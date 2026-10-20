# Stream Schedule Link

**Use it:** https://saltydayn.github.io/web-tools/schedule-link/

A streamer enters their weekly schedule (plus special one-off streams and days off) in their own
time zone and gets one link. Viewers who open it see every stream in their own local time, a live
countdown to the next one, and can add streams to their calendar (.ics). The streamer can also export
a schedule image (square, story, wide, Twitch panel). Accent color + dark/light theme.
No server, no account: the whole schedule lives inside the link. Part of the H.E.R.M.E.S. tool family.

## Files
- `index.html` - the whole tool, self-contained (~90 KB). This is what gets served.
- `src/` - `src.html` + `build.py` produce `index.html` (inlines the logo).

## How the link works
`schedule-link/#<code>` = viewer page. `#e<code>` = load that schedule into the editor ("Streamer? Edit this schedule").
`<code>` is a version char + base64url: `1` = deflate-raw compressed, `0` = plain UTF-8 JSON (whichever is shorter).
The hash is never sent to GitHub, so the schedule stays between streamer and viewer.

Payload (JSON array, trailing empty fields dropped):
```
[1, name, channelUrl, ianaTimeZone, accentHex(no #), light(0|1),
 slots: [[dayMask, startMin, endMin, title, game], ...],   dayMask bit 0 = Monday; end <= start = ends next day
 ones:  [[epochDay, startMin, endMin, title, game], ...],  one-off streams; epochDay = days since 1970-01-01
 offs:  [[fromEpochDay, toEpochDay, label], ...]]          days off, inclusive; to omitted = single day
```
Everything decoded is clamped and validated (lengths, ranges, http(s)-only links, valid time zone).
Changing the version number means old links need a migration path in `unpack()`.

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
