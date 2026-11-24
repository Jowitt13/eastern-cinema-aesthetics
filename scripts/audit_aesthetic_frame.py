"""Quantitative Aesthetic QC Auditor (v2.0) for Eastern Classical Cinema & Game Environments."""

import argparse
import json
import os
import subprocess
import sys
import numpy as np

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PALETTES_JSON = os.path.join(SKILL_DIR, "resources", "palettes.json")


def analyze_image(img_path, mood="hupojin"):
    if not os.path.exists(img_path):
        print(f"[ERROR] File not found: {img_path}")
        return 2

    with open(PALETTES_JSON, "r", encoding="utf-8") as fp:
        cfg = json.load(fp)
    if mood not in cfg["moods"]:
        print(f"[ERROR] Unknown mood '{mood}'. Choose from: {list(cfg['moods'].keys())}")
        return 2
    spec = cfg["moods"][mood]

    w, h = 320, 320
    cmd = [
        "ffmpeg", "-v", "error", "-i", img_path,
        "-vf", f"scale={w}:{h}:force_original_aspect_ratio=decrease",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-",
    ]
    raw = subprocess.run(cmd, capture_output=True).stdout
    if len(raw) < 300:
        print(f"[ERROR] Could not decode image via ffmpeg: {img_path}")
        return 2

    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", img_path],
        capture_output=True, text=True,
    ).stdout.strip().split(",")
    orig_w, orig_h = int(probe[0]), int(probe[1])
    if orig_w >= orig_h:
        sw, sh = 320, max(1, int(round(320 * orig_h / orig_w)))
    else:
        sh, sw = 320, max(1, int(round(320 * orig_w / orig_h)))

    arr = np.frombuffer(raw, dtype=np.uint8).astype(np.float32) / 255.0
    n_pix = len(arr) // 3
    arr = arr[: n_pix * 3].reshape(-1, 3)

    lum = 0.2126 * arr[:, 0] + 0.7152 * arr[:, 1] + 0.0722 * arr[:, 2]
    cmax, cmin = arr.max(axis=1), arr.min(axis=1)
    sat = np.where(cmax > 1e-4, (cmax - cmin) / (cmax + 1e-6), 0.0)

    shadow_pct = float((lum < 0.28).mean() * 100.0)
    mid_pct = float(((lum >= 0.28) & (lum < 0.72)).mean() * 100.0)
    hi_pct = float((lum >= 0.72).mean() * 100.0)
    vis = lum >= 0.08
    mean_sat = float((sat[vis].mean() if vis.any() else sat.mean()) * 100.0)

    edge_ratio_str = "N/A"
    border_darker = True
    if sw * sh == n_pix:
        grid = lum.reshape(sh, sw)
        by, bx = max(1, int(sh * 0.14)), max(1, int(sw * 0.14))
        center_lum = float(grid[by:-by, bx:-bx].mean())
        mask = np.ones((sh, sw), dtype=bool)
        mask[by:-by, bx:-bx] = False
        border_lum = float(grid[mask].mean())
        edge_ratio_str = f"border={border_lum:.3f} vs center={center_lum:.3f}"
        border_darker = border_lum <= center_lum * 1.04

    s_lo, s_hi = spec["target_shadow_pct"]
    h_lo, h_hi = spec["target_highlight_pct"]
    sat_lo, sat_hi = spec["target_sat_pct"]

    issues = []
    if shadow_pct < s_lo:
        issues.append(f"SHADOWS TOO BRIGHT ({shadow_pct:.1f}% < {s_lo:.0f}%): deepen shadows or add dark foreground framing.")
    if hi_pct > h_hi:
        issues.append(f"HIGHLIGHT FLOODING ({hi_pct:.1f}% > {h_hi:.1f}%): roll off highlights (-10..-19 EV) & add soft halation.")
    if mean_sat > sat_hi:
        issues.append(f"SATURATION TOO CANDY/CG ({mean_sat:.1f}% > {sat_hi:.0f}%): desaturate toward muted cinema palette.")
    if spec.get("require_dark_border", True) and not border_darker:
        issues.append(f"WEAK EDGE FRAMING ({edge_ratio_str}): edges brighter than center; add dark canopy/window/vignette occlusion.")

    status = "PASS" if not issues else "NEEDS_LOOKDEV_FIX"
    print(f"=== Aesthetic Audit v2.0 [{status}] | {os.path.basename(img_path)} | Mood: {mood} ({spec['name_zh']}) ===")
    print(f"  Shadows (<0.28):   {shadow_pct:5.1f}%  (target {s_lo:.0f}%..{s_hi:.0f}%)")
    print(f"  Midtones:          {mid_pct:5.1f}%")
    print(f"  Highlights (>0.72):{hi_pct:5.1f}%  (target {h_lo:.1f}%..{h_hi:.1f}%)")
    print(f"  Mean Saturation:   {mean_sat:5.1f}%  (target {sat_lo:.0f}%..{sat_hi:.0f}%)")
    print(f"  Edge Framing:      {edge_ratio_str}")
    for msg in issues:
        print(f"  [!] {msg}")
    return 0 if not issues else 1


if __name__ == "__main__":
    with open(PALETTES_JSON, "r", encoding="utf-8") as _fp:
        _moods = list(json.load(_fp)["moods"].keys())
    ap = argparse.ArgumentParser()
    ap.add_argument("image", help="Path to render or game screenshot")
    ap.add_argument("--mood", default="hupojin", choices=_moods)
    args = ap.parse_args()
    sys.exit(analyze_image(args.image, args.mood))
