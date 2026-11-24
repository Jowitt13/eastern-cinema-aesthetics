# Classic Film-Grading Presets & Progressive Weather Ramps

Distilled from Batch 2's curated cinema color-grading reference cards (`AUGUA` 7 master film looks) and 4-stage progressive morning mist sequences.

---

## 1. The Universal Film-Glow Law (压高光 + 提柔光)

Across every film-grading reference in the user's library, **two parameters appear in 100% of looks**:
1. **Highlights Pulled Down (`-10` to `-19`)**: Prevents harsh digital white clipping in sunlit skies, mist, and translucent leaves.
2. **Optical Soft-Glow / Halation Pushed High (`柔光 +30` to `+80`)**: Mimics classic vintage cinema glass + Black Pro-Mist filters where bright foliage gaps, lanterns, and mist spill a dreamy luminous halo into neighboring dark shadows.

### The 7 Curated Cinema Grading Presets (Ready for Compositor / UE5 LUTs)

| Preset ID | Reference Film / Painting | Core Slider DNA | Best Environment / Mood Match |
| :--- | :--- | :--- | :--- |
| **`van_gogh_almond`** | 梵高《盛开的杏花》(1890) | Exp `+25`, Hi `-10`, Shd `-15`, Temp `-30`, Tint `-30`, **Glow `+80`** | Looking up through gnarled dark branches into dreamy cyan-turquoise luminous blossoms (`senyou` / spring) |
| **`in_the_heat_of_sun`** | 姜文《阳光灿烂的日子》(1994) | Exp `+25`, Hi `-10`, Shd `-10`, Tint `-10`, **Glow `+80`** | Molten caramel-gold backlit dust, sun-drenched silhouettes, warm nostalgic haze (`hupojin`) |
| **`the_crossing`** | 《过春天》(2018) | Hi `-17`, Contrast `+21`, Vib `+37`, Temp `-27`, **Glow `+50`** | Humid blue-cyan rain glass, wet dusk alleys, luminous aquatic cool mood (`tianshuibi`) |
| **`raise_red_lantern`** | 张艺谋《大红灯笼高高挂》(1991) | Exp `+20`, Hi `-19`, Contrast `+13`, Shd `+21`, Temp `+15`, Tint `-25`, **Glow `+50`** | Formal crimson courtyards, long raking afternoon shadows, solemn warm-red drama (`hupojin` / palace) |
| **`journey_to_west`** | 《宇宙探索编辑部》(2021) | **Exp `-20`**, Hi `-16`, Shd `-10`, Temp `+35`, Tint `+20`, **Glow `+30`** | Underexposed desaturated cool slate-green poetic melancholy (`muyun` / overcast autumn) |
| **`double_life_veronique`** | 基耶斯洛夫斯基《两生花》(1991) | Exp `+25`, Hi `-10`, Shd `-10`, Tint `-10`, **Glow `+80`** | Deep umber-brown crushed shadows paired with painterly amber-gold sky & stained-glass warmth (`qijing_lacquer` / `hupojin`) |
| **`hello_mr_tree`** | 《Hello! 树先生》(2011) | Hi `-16`, **Contrast `+42`**, Temp `+15`, Tint `-29`, **Glow `+40`** | Surreal crisp emerald-teal foliage with heavy high-contrast dark shadows (`senyou`) |

---

## 2. Four-Stage Progressive Morning Mist Ramp (动态晨雾与游戏时间天气曲线)

Directly modeled on the curated 4-frame progressive lakeside autumn mist sequence (`IMG_8075`, `IMG_8077–8080`). Use this exact progression for **cinematic time-lapse arcs** or **UE5 Dynamic Weather Transitions**:

| Stage | Atmosphere State | Blender Bounded `Principled Volume` Density | UE5 `ExponentialHeightFog` Density | Visual Read |
| :--- | :--- | :--- | :--- | :--- |
| **Stage 1** | **清朗秋镜 (Clear Crisp Dawn)** | `0.002` (`Aniso 0.65`) | `0.005` (`HeightFalloff 0.25`) | Vibrant red/gold trees & sharp full lake reflections; only distant mountain base softens |
| **Stage 2** | **水面浮岚 (Low Water Mist)** | `0.009` (`Aniso 0.68`) | `0.018` (`HeightFalloff 0.45` low-clamped) | Silvery ribbon of mist hugs the water surface and tree roots; upper canopies still glow clearly |
| **Stage 3** | **晨雾半掩 (Luminous Veil)** | `0.022` (`Aniso 0.70`) | `0.042` (`Volumetric Scattering 2.5`) | Background hills vanish into soft milky cyan; midground crimson maples float like pastel watercolor |
| **Stage 4** | **水墨化无 (Monochrome Ink Fog)** | `0.045` (`Aniso 0.60`) | `0.085` (`MaxOpacity 0.92`) | Entire vista dissolves into calm desaturated blue-grey ink silhouettes (`天水碧` / `暮云灰` transition) |

---

## 3. Translating High Halation (`柔光 +50..+80`) Without Looking Like Cheap Neon

- **Never use a single low-threshold wide bloom** (that makes everything milky and washed out).
- **Use a Dual-Stage Filmic Halation Stack**:
  1. **Tight Warm Highlight Halo**: `Threshold = 1.10`, small radius (`Size 6` in Cycles `Fog Glow` / tight Convolution kernel in UE5), subtle strength `0.18–0.28` — softens high-contrast edges between bright sky and dark tree twigs!
  2. **Wide Subtle Atmospheric Diffusion**: `Threshold = 1.65`, wide radius (`Size 8–9`), very gentle strength `0.08–0.14` — mimics Black Pro-Mist `1/4` or `1/2` glass filter wrapping sunlit gaps and fire cores in silky cinema air.
