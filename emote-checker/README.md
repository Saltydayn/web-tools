# Emote & Badge Checker

**Use it:** https://saltydayn.github.io/web-tools/emote-checker/

Free, browser-only tool: drop one PNG/GIF, get every size for Twitch emotes, Twitch sub badges,
7TV and Discord, a fake-chat preview (dark + light), problem checks, and a single zip.
Nothing is uploaded; no network requests at all. Part of the H.E.R.M.E.S. tool family.

## Files
- `index.html` - the whole tool, self-contained (~84 KB). This is the only file you host.
- `src/` - editable source. `src.html` + `build.py` produce `index.html`
  (inlines the logo and the GIF library). Run: `python build.py` inside `src/`, then copy the
  resulting `index.html` up one folder.

## Hosting
Part of the Saltydayn Tools site (see the README one folder up). Push = deploy (about 1 minute).

## Limits used (checked Oct 2026)
| Platform | Sizes | Limit |
|---|---|---|
| Twitch emote, static | 28 / 56 / 112 PNG | 1 MB each |
| Twitch emote, animated | 28 / 56 / 112 GIF | 512 KB each, max 60 frames, max 3 flashes/s |
| Twitch sub badge | 18 / 36 / 72 PNG | 25 KB each |
| 7TV | one file, max 1000x1000 (exported at up to 512) | 7 MB, max 1000 frames |
| Discord emoji | 128 | 256 KB (auto-shrinks to 96/64 if a GIF is too big) |

Change them in `src.html` (the `LIM` object) if a platform changes its rules.

## Third-party code (MIT)
- gifenc - Matt DesLauriers
- gifuct-js - Matt Way

## License
Source-available, not open source. Free to use (including for monetized channels and commission work); the images you make are yours. Don't copy, re-host or rebrand the tool without asking. See [LICENSE](../LICENSE).
