---
name: eastern-cinema-aesthetics
description: >-
  Eastern Classical Cinema & Game Environment Art Direction System (v2.0) distilled from 167 curated
  references (Nepter, Yangliujin, Kyoto Rurikoin/Genko-an, Suzhou/West Lake/Forbidden City, Dolomites
  monumental scale, and 7 classic film color-grading recipes). Use whenever designing, directing,
  lighting, shading, composing, grading, or reviewing 3D film scenes, Blender Cycles renders,
  Unreal Engine 5 / Unity game environments, level art vistas, dynamic weather ramps, white-model-to-render
  reveals, or concept art in a poetic, restrained, high-halation atmospheric style ("幽、深、润、古、寂、藏、巨").
---

# Eastern Classical Cinema & Game Environment Aesthetic System (v2.0)

A quantitative, cross-engine art-direction and lookdev system distilled from **167 curated stills and cinema clips** (`149` stills + `18` videos) for **3D films (Blender 5.2 Cycles)** and **real-time game environments (UE5 Lumen / Unity HDRP)**.

> **Core Emotional Thesis — 「幽、深、润、古、寂、藏、巨」**
> *Crushed shadows that quiet the mind; abundant foliage, gauze veils, and dark timber frames that conceal more than they reveal; rolled-off highlights wrapped in filmic optical halation (`柔光`); alternating between intimate tactile poetry and monumental mountain-scale solitude.*

---

## 1. Non-Negotiable Visual Constitution (Measured Across 149 Stills)

1. **The 45 / 50 / 5 Luminance Law**:
   - **Shadows (`lum < 0.28`)**: **`42% – 65%`** (Batch 1 median `41.8%`, Batch 2 median `46.2%`, dark lacquer interiors up to **`67.6%`**).
   - **Midtones (`0.28 – 0.72`)**: **`40% – 52%`**.
   - **Highlights (`lum > 0.72`)**: **`0.2% – 9.5%`** (combined median **`~4.4%`**). **Always pull Highlights DOWN (`-10` to `-19`)** so bright leaves, mist, and sky never clip flat white.
2. **Restrained Film Saturation**: Target mean saturation **`24% – 48%`** (Batch 2 median **`34.7%`**).
3. **High Optical Halation（「压高光 + 提柔光」双核心定律）**:
   - Across all curated film-grading cards, every master grade combines **rolled-off highlights** with **strong optical soft-glow / Black Pro-Mist halation (`柔光 +30` to `+80`)** so light blooms tenderly out of leaf crevices, mist veils, candles, and water glints into surrounding darkness.
4. **Concealment (`藏`) & Scale Contrast (`巨`)**:
   - Either **wrap `45%–70%` of the frame** in dark occlusion (lacquer rooms, window mullions, overhanging boughs, translucent silk/calligraphy curtains, soft bokeh foliage) OR **dwarf tiny architecture (`< 3%` frame area)** against monumental cliffs/forests (`80%–90%` frame mass).
5. **Living Micro-Accents（「画眼 / 灵气点睛」）**:
   - Anchor still environments with one quiet sign of life: a ginger cat sleeping in a sunbeam at a temple gate, two deer on red maple leaves, circling birds above dark eaves, tiny ducks/boats trailing ripples across misty water, or a lone distant back-view umbrella silhouette (`< 8%` height).

---

## 2. Seven Canonical Mood Palettes

Machine-readable HEX / sRGB / Cycles-Linear / UE5-Linear tokens live in [resources/palettes.json](./resources/palettes.json) *(optional personal reference moodboards may be placed locally in `resources/moodboard_*.jpg`, gitignored by default)*.

| Mood Key | Traditional Name | Visual Signature | Shadow / Highlight Target |
| :--- | :--- | :--- | :--- |
| **`tianshuibi`** | **天水碧 · 青黛烟雨** | Slate-cyan mist (`#516e7d`), deep pine-ink shadows (`#0d191a`), blurred lotus/reeds, lone warm lantern | Shadows `~50%`, Hi `< 3.5%` |
| **`hupojin`** | **琥珀金 · 浓墨金秋** | Deep umber trunks (`#1c130a`), burning vermilion maples (`#b82b18`), translucent ginkgo gold (`#e4a322`), cool muted sky | Shadows `~49%`, Hi `1%–9.5%` |
| **`senyou`** | **森幽绿 · 丁达尔清夏** | Dense bamboo/cedar shadows (`#0f110e`) sliced by warm volumetric morning god-rays (`#e2d4cc`) | Shadows `~40%`, Hi `1.5%–10%` |
| **`muyun`** | **暮云灰 · 素墨留白 / 高级白模** | Desaturated ink-grey / snow negative space (`#131512` → `#a69e9b`) for snow scenes & **Clay-to-Render reveals** | Shadows `~53%`, Hi `0.5%–9%` |
| **`qijing_lacquer`** | **漆镜幽秋 · 琉璃光院式暗室** | Pitch-dark timber hall (`#170d06`, **`~68%` shadow!**) with polished black-lacquer table/floor mirroring glowing autumn windows | Shadows `55%–78%`, Hi `< 4%` |
| **`ember_indigo`** | **烬焰暮蓝 · 戏剧孤火夜枝** | Deep twilight cobalt-indigo (`#293a5d`) shattered by burning temple flame, altar candles, or glowing night-sky gold leaves | Shadows `46%–68%`, Hi `< 5%` |
| **`jushan_monolith`** | **巨山微屋 · 苍灰神性尺度** | Low-saturation monumental granite cliffs & dark pine walls (`#2e433f` → `#92a7b3`, sat `~24%`) dwarfing tiny quiet architecture | Shadows `22%–48%`, Hi `< 14%` |

---

## 3. Reference Modules (Load As Needed)

- **10 Composition & Vista Blueprints + Micro-Life Accents**: [references/composition-and-framing.md](./references/composition-and-framing.md)
- **Color Science, Luminance Law & High-Taste Clay Standard**: [references/color-palettes-and-lighting.md](./references/color-palettes-and-lighting.md)
- **7 Classic Film-Grading Presets & 4-Stage Progressive Mist Ramps**: [references/film-grading-and-weather-ramps.md](./references/film-grading-and-weather-ramps.md)
- **Dual-Engine Implementation (Blender 5.2 Cycles & UE5 Lumen / Unity)**: [references/engine-recipes-blender-ue5.md](./references/engine-recipes-blender-ue5.md)
- **Anti-CG-Plastic Redlines & 5-Point Sign-Off Rubric**: [references/anti-patterns-and-qc-rubric.md](./references/anti-patterns-and-qc-rubric.md)

---

## 4. Mandatory Automated Aesthetic Audit Gate

Before approving any film still, Blender lookdev pass, or UE5/Unity game screenshot, run:

```bash
python scripts/audit_aesthetic_frame.py <image_path> --mood <tianshuibi|hupojin|senyou|muyun|qijing_lacquer|ember_indigo|jushan_monolith>
```

Inspect **both** the numeric audit report and the actual pixels against [references/anti-patterns-and-qc-rubric.md](./references/anti-patterns-and-qc-rubric.md).
