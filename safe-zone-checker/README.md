# Shorts Safe-Zone Checker

**Use it:** https://saltydayn.github.io/web-tools/safe-zone-checker/

Drop a vertical image or video and see what TikTok, Instagram Reels and YouTube Shorts cover
(top bar, buttons, caption). Toggle platforms, use the combined view for the area that's safe on all
three, scrub through video frame by frame, and export a transparent overlay PNG for your editor.
Runs fully in the browser; nothing is uploaded. Part of the H.E.R.M.E.S. tool family.

## Files
- `index.html` - the whole tool, self-contained (~77 KB). This is what gets served.
- `src/` - `src.html` + `build.py` produce `index.html` (inlines the logo).

## Updating the zones (the only place to edit)
In `src/src.html`, the `<script type="application/json" id="zone-data">` block at the top.
Each platform has a list of boxes in pixels on a 1080x1920 frame (`x`, `y` from the top-left,
`w`, `h` = size). `edge: true` = thin side strip that tall phones may crop. Change the numbers,
update `checked` and `sources`, rebuild. It's plain JSON, so HERMES can read the same block later.

## Zones used (organic posts, checked Oct 2026)
Measured estimates, not official: no platform publishes organic numbers, and sources disagree by
up to ~150 px (especially the YouTube top bar and all caption areas). Values lean safe.

| Platform | Top bar | Buttons column | Caption area | Side edges | Biggest clear area |
|---|---|---|---|---|---|
| TikTok | y 0-200 | x 930-1080, y 760-1560 | y 1560-1920 | 60 px | 870 x 1360 |
| Instagram Reels | y 0-250 | x 960-1080, y 1000-1580 | y 1580-1920 | 40 px | 920 x 1330 |
| YouTube Shorts | y 0-240 | x 880-1080, y 820-1530 | y 1530-1920 | 48 px | 832 x 1290 |
| **All three** | | | | | **820 x 1280 at x 60, y 250** |

Ads reserve much more at the bottom (TikTok/YouTube ad templates: bottom ~670 px). Not modeled.

## Notes
- Video uses whatever the browser can play: MP4 (H.264) and WebM everywhere, MOV mostly.
  MKV doesn't play in browsers (OBS: File > Remux Recordings to get an MP4).
- Frame stepping assumes 30 fps (browsers don't expose the real frame rate).
