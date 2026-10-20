# Saltydayn Tools

**Live:** https://saltydayn.github.io/web-tools/

Small free browser tools for streamers and creators, part of the H.E.R.M.E.S. family.
Every tool is one self-contained `index.html`: no server, no tracking, nothing uploaded.

| Tool | Folder | Live |
|---|---|---|
| Emote & Badge Checker | `emote-checker/` | https://saltydayn.github.io/web-tools/emote-checker/ |
| Shorts Safe-Zone Checker | `safe-zone-checker/` | https://saltydayn.github.io/web-tools/safe-zone-checker/ |
| Stream Schedule Link | `s/` (old address `schedule-link/` forwards here) | https://saltydayn.github.io/web-tools/s/ |

## Layout
- `index.html` - the tool list (landing page).
- `<tool>/index.html` - the built tool. This is what gets served.
- `og.jpg` / `<tool>/og.jpg` - 1200x630 link-preview image (Discord, X, Ko-fi embeds). Referenced by the
  `og:` meta tags in each page's `<head>`. Optional for the tool to work; only matters for shared links.
- `<tool>/src/` - editable source + `build.py` (inlines the logo, and libraries where needed).
  Run `python build.py` inside `src/`, then move the new `index.html` up one folder.

## Shared rules for every tool
- Same look (HERMES colors/fonts), same header link buttons (Ko-fi, GitHub, Links).
- The "Liked this?" popup uses the localStorage key `hermes.tools.promoShown`. All tools live on
  the same site, so it shows **once across all tools**, never per tool. Keep that key when adding a tool.
- Adding a tool: new folder, then add a card to the root `index.html` and a row to this table.
  Copy the `og:` meta block from another tool and make an `og.jpg` for it.
- The landing page also has an "Also by Saltydayn" row (H.E.R.M.E.S., link page). Those are other
  projects, not tools here, so they use the dashed `.proj` style instead of tool cards.

## Hosting
GitHub Pages, branch `main`, folder `/ (root)`. Push = deploy (about 1 minute).

## License
Source-available, not open source. See [LICENSE](LICENSE).
