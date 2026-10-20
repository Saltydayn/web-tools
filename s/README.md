# Stream Schedule Link

**Use it:** https://saltydayn.github.io/web-tools/s/

Lives at `s/` to keep share links short. `schedule-link/` is a one-line page that forwards there (hash included), so the first links ever made still work.

A streamer enters their weekly schedule (plus special one-off streams and days off) in their own
time zone and gets one link. Viewers who open it see every stream in their own local time, a live
countdown to the next one, and can add streams to their calendar (.ics). The streamer can also export
a schedule image (square, story, wide, Twitch panel). Accent color + dark/light theme.
No server, no account: the whole schedule lives inside the link. Part of the H.E.R.M.E.S. tool family.

## Files
- `index.html` - the whole tool, self-contained (~95 KB). This is what gets served.
- `src/` - `src.html` + `build.py` produce `index.html` (inlines the logo).

## How the link works
`s/#<code>` = viewer page. `#e<code>` = load that schedule into the editor ("Streamer? Edit this schedule").
`<code>` = one version character + base64url. The hash is never sent to GitHub.

| Prefix | Format | Written today? |
|---|---|---|
| `2` | compact binary (`packBin`) | yes |
| `3` | compact binary, deflate-compressed (used only when shorter, i.e. big schedules) | yes |
| `1` | deflated JSON (first release) | no, decode only |
| `0` | plain JSON (first release) | no, decode only |

Binary layout (varint = 7 bits per byte; str = varint byte length + UTF-8):
```
varint flags      bit0 light, bit1 name doubles as channel handle, bit2 custom color, bit3 time zone not in table
u8     platform   0 none, 1 Twitch, 2 YouTube @handle, 3 Kick, 4 TikTok @handle, 255 other link (stored in full)
[str handle | str url]   handle only if platform 1-4 and bit1 is off
str    name
tz     varint index into TZ_TABLE, or str if bit3
color  varint index into ACCENTS, or 3 raw bytes if bit2
slots  varint n, then n x (u8-ish varint dayMask, time start, time end, str title, str game)
ones   varint n, then n x (zigzag day-20000, time, time, str title, str game)
offs   varint n, then n x (zigzag from-20000, varint length-in-days, str label)
time   varint: quarter hours (0-95) as-is, any other minute as 96 + minutes
```
**`TZ_TABLE`, `ACCENTS` and `PLATFORMS` are append-only.** Links store positions in them, so reordering or removing
an entry silently breaks existing links. Add new entries at the end only.
Both decoders return the same array as the old JSON format and go through one `unpack()`, so validation is shared.

Everything decoded is clamped and validated (lengths, ranges, http(s)-only links, valid time zone).


## Time zones / daylight saving
Times are stored as the streamer's wall-clock times plus their IANA zone. Each concrete date is
converted to an instant with `Intl` (`wallToUtc`), so DST changes in either zone come out right,
including the weeks where Europe and the US switch on different dates. Times that don't exist
(clocks jump forward) move forward by the gap; ambiguous times (clocks go back) use the first one.
Calendar files use `TZID` + a generated `VTIMEZONE` (12 years of explicit transitions), weekly
`RRULE`s, and `EXDATE`s for days off.

## Rules kept from the other tools
- Corner buttons only in the editor. Viewers (the streamer's audience) get just a small footer link.
- The "Liked this?" popup shows after the first created link, never on the viewer page, and uses the
  shared `hermes.tools.promoShown` key (once across all tools).
- The streamer's draft is saved in the browser (`hermes.tools.schedule.draft`).

## Known limits
- A changed schedule means a new link; already-posted links keep the old schedule.
- Link previews (Discord etc.) show the tool's generic title, not the streamer's name: the data is in the
  hash, which preview bots don't run.
- The social image shows the schedule in the streamer's time zone (an image can't convert per viewer) and is English-only.
