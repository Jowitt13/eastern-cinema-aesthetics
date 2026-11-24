# Eastern Cinema Aesthetics (`eastern-cinema-aesthetics`)

A cross-agent [AgentSkills](https://agentskills.io) art-direction & lookdev system (v2.0) distilled from **167 curated visual references** for **3D films (Blender 5.2 Cycles)** and **real-time game environments (UE5 Lumen / Unity HDRP)**.

一套可跨 Agent 复用的 **东方古典电影与游戏场景审美指导 Skill（v2.0）**，基于 167 份精选电影摄影与东方古建参考系统量化提炼，沉淀了 **「幽、深、润、古、寂、藏、巨」** 的核心影调法则、7 大线性色板 Token、10 大构图蓝图、7 套经典电影调色与高柔光配方、4 阶动态晨雾曲线，以及开箱即用的自动化审片脚本。

> Pairs cleanly with [`Jowitt13/blender-programmatic-cinema`](https://github.com/Jowitt13/blender-programmatic-cinema) for end-to-end script-driven Blender 5.2 Cycles short films.

---

## What's Inside / 目录结构

```text
eastern-cinema-aesthetics/
├── SKILL.md                                  # Core aesthetic constitution, 45/50/5 luminance law & 7 moods
├── references/
│   ├── composition-and-framing.md            # 10 framing & game-vista blueprints + living micro-accents
│   ├── color-palettes-and-lighting.md        # Luminance discipline, backlit grazing light & Muyun Clay standard
│   ├── film-grading-and-weather-ramps.md     # 7 classic film-grading presets (high halation) + 4-stage mist ramp
│   ├── engine-recipes-blender-ue5.md         # Dual-engine recipes: Blender 5.2 Cycles & UE5 Lumen / Unity HDRP
│   └── anti-patterns-and-qc-rubric.md        # 10 anti-CG-plastic redlines + 5-point visual sign-off rubric
├── resources/
│   └── palettes.json                         # Machine-readable HEX / sRGB / Linear RGB tokens & ramps
└── scripts/
    └── audit_aesthetic_frame.py              # Quantitative luminance, saturation & dark-edge framing QC gate
```

---

## Install Into Your Agent / 安装方式

Clone this repository directly into your agent's `skills/` directory:

- **Antigravity (Global)**:
  ```bash
  git clone https://github.com/Jowitt13/eastern-cinema-aesthetics.git ~/.gemini/config/skills/eastern-cinema-aesthetics
  ```
- **Claude Code (Global)**:
  ```bash
  git clone https://github.com/Jowitt13/eastern-cinema-aesthetics.git ~/.claude/skills/eastern-cinema-aesthetics
  ```
- **Codex (Global)**:
  ```bash
  git clone https://github.com/Jowitt13/eastern-cinema-aesthetics.git ~/.codex/skills/eastern-cinema-aesthetics
  ```
- **Project-Level / Cursor / Universal `.agents`**:
  ```bash
  git clone https://github.com/Jowitt13/eastern-cinema-aesthetics.git .agents/skills/eastern-cinema-aesthetics
  ```

---

## Highlights / 核心亮点

- **Empirical Film-Science Constitution (`45 / 50 / 5` Law)**: Grounded in pixel-level luminance & saturation measurement across 149 stills — anchors `42%–65%` deep shadow gravity, `< 5%–10%` precious rolled-off highlights, and `24%–48%` restrained cinema saturation.
- **7 Canonical Moods (`resources/palettes.json`)**: `tianshuibi` (天水碧·青黛烟雨), `hupojin` (琥珀金·浓墨金秋), `senyou` (森幽绿·丁达尔清夏), `muyun` (暮云灰·素墨白模), `qijing_lacquer` (漆镜幽秋·琉璃光院式暗室), `ember_indigo` (烬焰暮蓝·戏剧孤火), and `jushan_monolith` (巨山微屋·神性尺度).
- **10 Reusable Composition Blueprints**: Covers overhanging botanical canopies, extreme dark-frame-to-bright portals, translucent backlit macro poetry (oil-paper umbrella / wall shadows), lacquer-mirror rooms, monumental mountain scale vistas, translucent calligraphy gauze veils, and 90° top-down courtyard symmetry.
- **High-Halation Grading & Dynamic Weather**: Encodes the **"Roll-Off Highlights + High Optical Soft-Glow (Black Pro-Mist)"** formula across 7 classic film looks and a 4-stage progressive morning mist ramp (`清朗倒影 → 水面浮岚 → 晨雾半掩 → 水墨化无`).
- **Automated Lookdev QC Gate**: Run `python scripts/audit_aesthetic_frame.py <render.png> --mood <mood>` (requires `numpy` + `ffmpeg`) to catch blown highlights, flat bright shadows, candy saturation, or weak edge framing before committing long render passes or shipping game levels.

---

## Quick Usage / 审片脚本快速使用

```bash
python scripts/audit_aesthetic_frame.py path/to/render.png --mood tianshuibi
python scripts/audit_aesthetic_frame.py path/to/lacquer_room.png --mood qijing_lacquer
python scripts/audit_aesthetic_frame.py path/to/cliff_vista.png --mood jushan_monolith
```

---

## License

MIT License — see [LICENSE](./LICENSE).
