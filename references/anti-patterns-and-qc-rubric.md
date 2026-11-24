# Anti-CG-Plastic Redlines & Visual QC Rubric

Audit EVERY hero render, game screenshot, or lookdev still against these **10 hard redlines** before presenting or shipping. Any single redline failure requires fixing before sequence rendering or level sign-off.

---

## The 10 Instant-Reject Anti-Patterns ("低幼 3D / 网游塑料感" 红线)

1. **Real-Estate Diorama Framing (居中沙盘孤楼)**: A complete symmetrical pavilion sitting exposed in the exact center of an empty lake with zero dark foreground occlusion.
2. **Toothpick Trees (牙签稀疏树)**: Thin uniform cylinder trunks with sparse, countable floating leaf planes instead of gnarled dark trunks + dense multi-layered canopy mass.
3. **Anime Candy Sky / Cartoon Space FX (糖水渐变与塑料特效)**: Oversaturated royal-blue gradient skies, bright cartoon meteor bars, or glowing white spherical firefly balls that scream "cheap 3D CG".
4. **Blown-Out White Walls / Highlight Flooding (`> 14%` pixels above `0.72` lum)**: Flat bright plaster walls or washed-out skies killing the dark-to-bright mystery.
5. **Sterile Unweathered Surfaces (无时间感的光滑塑料)**: Perfectly clean uniform bricks, spotless white walls with zero damp moss plinth (`勒脚`), or empty swept stone paths with zero fallen leaves.
6. **Chrome-Mirror Flat Water**: Perfectly flat untextured water plane reflecting a sun blob; real garden water has deep jade absorption, gentle painterly wave distortion, and floating debris/petals.
7. **Auto-Exposure Ruining Dark Portals**: Letting camera auto-exposure brighten a dark interior corridor until the garden outside blows out into solid white.
8. **Uncanny Close-Up Digital Humans**: Putting procedural or low-craft human faces near the camera. Keep figures distant (`< 8%` frame height), back-view, veiled by oil-paper umbrellas, or omit entirely in favor of living botanical/light storytelling.
9. **Billboards Turning Into Squares in Clay Mode**: Blind `material_override` wiping out leaf alpha channels during white-model passes.
10. **Uncoupled Text / Cluttered Overlays**: Generic bright UI fonts floating randomly over imagery instead of quiet, minimal classical restraint (or text-free raw beauty).

---

## 5-Point Sign-Off Rubric (Pass = All 5 Green)

| Gate | Question to Ask Yourself Looking at the Pixels | Target |
| :--- | :--- | :--- |
| **1. Shadow Gravity** | Does ~40%–55% of the frame sit in rich, dark, calming shadows? | Run `audit_aesthetic_frame.py` (`shadows >= 35%`, `highlights <= 10%`) |
| **2. Concealment (`藏`)** | Are the edges framed by dark foreground foliage, eaves, windows, or mist rather than exposed void? | `>= 40%` perimeter framing/occlusion |
| **3. Botanical Mass** | Do trees/bamboo/lotus read as dense, layered, backlit living nature rather than sparse CG sticks? | No countable isolated leaf cards |
| **4. Air & Humidity** | Can you *feel* the moisture, morning haze, rain chill, or sunlit air between foreground, midground, and background? | Clear 3-layer depth separation |
| **5. Film Restraint** | If shown to a photographer without context, does the color & contrast feel like a real cinema still (`Nepter / 羊六斤`)? | Low-key traditional film color (`sat ~30%–50%`) |
