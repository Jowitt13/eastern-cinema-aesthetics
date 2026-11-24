# Color Science, Luminance Discipline & Film Lighting

Quantitative lighting and color-grading guide measured across the 86 reference stills & videos.

---

## 1. The 45 / 50 / 5 Luminance Law

Amateur 3D scenes fail by spreading brightness evenly across the frame (`25%–40%` highlights, washed-out shadows). Eastern classical cinema photography does the opposite:

- **Shadows (`lum < 0.28`)**: **`40% – 55%`** of frame area.
  - Keep deep shadows tinted with cool pine-ink (`#0d191a`) in mist/rain moods or warm burnt umber (`#1c130a`) in autumn moods — never flat washed-out neutral grey.
- **Midtones (`0.28 – 0.72`)**: **`40% – 52%`** of frame area.
  - This is where mist gradients, weathered stone, timber grain, damp walls, and shaded foliage live.
- **Highlights (`lum > 0.72`)**: **`0.2% – 9.5%`** (median **`3.5%`**).
  - Never allow plain white walls or huge sky patches to clip at pure white (`#ffffff`). Pull exposure down (`-0.25` to `-0.80 EV`) until bright foliage/mist gleams richly while retaining full texture.

---

## 2. Lighting Architecture Rules

1. **Directional Backlight & Grazing Side-Light First (`105° – 160°` off camera axis)**:
   - Place the Sun/Moon **behind or raking sharply across** foliage canopies and architectural eaves.
   - Backlighting turns maple leaves, ginkgo fans, oiled paper umbrellas, willow curtains, and volumetric mist into luminous translucent stained glass while naturally pushing trunks and foreground architecture into rich silhouette.
2. **Motivated Micro-Warmth Inside Cool Darkness**:
   - In `天水碧` blue-hour mist or twilight scenes, place **1–3 tiny motivated warm sources (`2600K–2900K`)** (a palace lantern under dark eaves, red candles in a dark hall, a faint warm glow on a distant boat). Keep their radius tight so they feel precious, never flooding the whole courtyard orange.
3. **Never Attach Global Volume to Infinite World (Cycles) / Over-Dense Fog (UE5)**:
   - Use **layered, height-clamped, bounded atmospheric mist** so light shafts pierce cleanly through trees and portals without turning distant skies muddy black.
4. **Black Pro-Mist / Film Halation Finish**:
   - Real cinema glass diffuses high-luminance leaf gaps, candle flames, and sunlit mist softly into adjacent dark pixels (`Fog Glow` / `Bloom` with high threshold `1.1–1.4`, low subtle mix `0.15–0.24`).
   - Add faint organic color-film grain (`1.5%–3%`) and a gentle optical vignette (`-0.3 to -0.6 EV` corners) to unify 3D assets with photographic truth.

---

## 3. High-Taste White-Model (`暮云灰` Clay) Lighting Standard

When designing **Clay-to-Render reveal shots** (`白模秒切渲染`):
- **Do NOT use flat grey ambient clay** (looks like an unfinished Viewport screenshot).
- **DO use sculpted `暮云灰` Monochrome Cinema Clay**:
  - Preserve **50%+ rich sculpted shadow depth** via strong `45°` raking key light + tight Ambient Occlusion crevices (`distance = 0.5–0.8m`).
  - Preserve **exact botanical alpha leaf silhouettes** on trees/bamboo so foliage looks like delicate carved white paper-cut art rather than grey billboard squares.
  - Keep sky in overcast layered monochrome clouds (`#373733` → `#b4b4b2`, never bright `#ffffff`).
  - Match the exact shadow direction to the incoming Color Render pass so the 1-frame beat-cut feels like **color and atmosphere flooding into a frozen sculpture** rather than a mismatched lighting swap!
