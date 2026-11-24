# Dual-Engine Implementation Recipes (v2.0 — Blender 5.2 Cycles & UE5 / Unity)

Concrete engineering parameters translating all 10 composition blueprints and 7 moods directly into film renders and real-time game environments.

---

## Part A: Blender 5.2 LTS + Cycles (Film / High-End Stills)

### 1. Color Management & Dual-Stage Halation Compositor
- **View Transform**: `AgX` | **Look**: `AgX - Medium High Contrast` (or `High Contrast` for `qijing_lacquer` / `ember_indigo`).
- **Exposure**: Typically `-0.20` to `-0.65` (keep highlights strictly `< 5%–9%`).
- **Compositor (Blender 5.2 `scene.compositing_node_group`)**:
  - Chain **two `CompositorNodeGlare` nodes** (`inputs["Type"].default_value = "Fog Glow"`) for authentic `柔光 +50..+80` cinema halation without washing out dark shadows:
    - Pass 1 (Tight Rim Softener): `Threshold = 1.15`, `Strength = 0.22`, `Size = 6`.
    - Pass 2 (Wide Pro-Mist Halo): `Threshold = 1.75`, `Strength = 0.10`, `Size = 8`.
  - Pair with subtle split-tone `Color Balance` (cool pine shadows for `tianshuibi` / `the_crossing`, warm umber shadows + golden highlights for `double_life_veronique` / `hupojin`).

### 2. Polished Black-Lacquer Mirror Interior (`qijing_lacquer` — Blueprint G)
- **Table / Floor Shader**: `Principled BSDF`, `Base Color = (0.008, 0.004, 0.002)` (`#170d06` Linear), `Roughness = 0.025–0.042` driven by subtle fine wood-grain `Noise` (`Scale = 18`, range `0.02..0.05`), `Coat Weight = 1.0`, `Coat Roughness = 0.015`, `Coat IOR = 1.54`.
- **Lighting**: Zero interior fill lights! Let 100% of room bounce come naturally from the bright sunlit maple foliage outside the circular/mullion window (`diffuse_bounces = 4`, `glossy_bounces = 4`).

### 3. Translucent Silk Gauze & Floating Calligraphy Banners (Blueprint I)
- **Geometry**: Subdivided cloth plane with gentle wind-wave displacement (`Wave/Cloth` modifier, subtle vertical folds).
- **Shader**: Mix `ShaderNodeBsdfTransparent` (`Alpha = 0.55–0.72` sheer silk weave, modulated by crisp black ink calligraphy strokes where `Alpha = 0.92` and `Base Color = #121210`) with a 50/50 `Principled BSDF + Translucent BSDF` (`#f4f2ec`) so grazing sunbeams illuminate the sheer silk fabric and floating brushwork against dark garden foliage behind!

### 4. Foliage Density & Translucent Canopy (Eliminating "Stick-Tree CG")
- **Density Rule**: Use **Geometry Nodes / Mesh Instancing** for **`3,000 – 25,000` curved 3D leaf clusters** per hero canopy across 3 zones:
  1. Dark interior core (`Value × 0.50`, opaque — builds true visual mass).
  2. Mid canopy clusters (`Object Info -> Random` Hue/Value shift).
  3. Backlit rim clusters (`Principled 52% + Translucent 48%`).
- **VRAM Guardrail (4GB–8GB GPUs)**: `transparent_max_bounces = 32`, shared `Mesh` instancing, `use_auto_tile = True`, Cycles `OPTIX` GPU denoiser.

### 5. Bounded Volumetric Fog & Monumental Aerial Perspective (Blueprints E & H)
- Never plug `Principled Volume` into infinite World Volume (extinguishes Sky & Sun).
- Use **bounded local fog boxes** calibrated to the 4-Stage Progressive Mist Ramp in [film-grading-and-weather-ramps.md](./film-grading-and-weather-ramps.md) (`Density = 0.002 → 0.009 → 0.022 → 0.045`).
- For **`jushan_monolith`** monumental cliff scenes: place a height-attenuated fog volume (`ShaderNodeSeparateXYZ -> Z -> MapRange` fading density to `0` above cliff mid-height) so foreground lakes stay crisp while towering granite ridges step back in atmospheric layers.

---

## Part B: Unreal Engine 5 (Lumen / Nanite) & Unity HDRP (Game Environments)

### 1. UE5 Lighting, Atmosphere & Dynamic Mist Ramp
- **Directional Light**: Low elevation (`10° – 24°`), placed `110° – 150°` opposing primary player sightlines; `Volumetric Scattering Intensity = 2.0 – 4.5`.
- **Sky Light**: Keep restrained (`0.35 – 0.60`) so Lumen indirect lighting preserves `45%–65%` deep shadow gravity (never flat ambient fill!).
- **Exponential Height Fog + Local Volumetric Fog**:
  - Drive `Fog Density` along the 4-stage ramp (`0.005 → 0.018 → 0.042 → 0.085`) via Material Parameter Collection / Time-of-Day curve for live weather moods.
  - Set `Fog Inscattering Color` from `resources/palettes.json` (`tianshuibi` Linear `[0.082, 0.156, 0.205]`; `jushan_monolith` Linear `[0.287, 0.386, 0.451]`).

### 2. UE5 PostProcessVolume (Film Halation & Highlight Roll-Off)
- **Exposure**: `Metering Mode = Manual` or locked `Min/Max EV100` (`±0.4` stop) — **critical** for Blueprint B (Dark Moon Gate) and Blueprint G (Black Lacquer Room) so UE5 Auto-Exposure doesn't ruin the dark foreground frame!
- **ACES Filmic Tonemapper**: `Slope = 0.90`, `Toe = 0.60–0.65` (anchors rich shadow depth), `Shoulder = 0.28–0.32` (replicates `-15` Highlight Roll-Off!).
- **Bloom (High Optical Halation `柔光 +50..+80`)**: Use `Method = Convolution` (with a soft Black Pro-Mist kernel, `Intensity = 0.45–0.75`) or `Standard` (`Threshold = 1.15`, `Intensity = 0.55`).
- **Vignette**: `0.35 – 0.48` | **Film Grain**: `0.08 – 0.14` | **Global Saturation**: `0.84 – 0.94`.

### 3. Game Shaders & Level-Art Sightline Dressing
- **Black Lacquer Mirror (`qijing_lacquer`)**: Enable **Lumen High-Quality Translucency/Hardware Ray-Traced Reflections** (`Roughness = 0.03`, `Clear Coat = 1.0`) inside dark wood rooms to get crisp real-time autumn mirror floors.
- **Gauze / Calligraphy Veils (`Blueprint I`)**: `Subsurface` / `Two Sided Foliage` + `World Position Offset` gentle sine-wind sway + opacity mask for drifting sunlit silk curtains at temple doorways.
- **Monumental Scale Sightlines (`jushan_monolith`)**: Use `85mm` cinematic camera sequences (or narrow gameplay FOV `55°–65°` at cliff lookouts) so massive background Nanite cliffs fill `80%+` of vertical screen space behind tiny warm village/shrine beacons.
