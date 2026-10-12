# Webcam Bridge

**For Cursor and Grok Bot.**

**Free, MIT.** MCP Apps buttons in chat → one JPEG in this conversation → camera released. No tray exe.

## Free vs Pro

| Tier | In this plugin |
| --- | --- |
| **Free** | Buttons **拍一张 / 再拍 / 关掉**; click capture → JPEG in chat; camera released |
| **Pro** | Placeholders only (连拍 / 录像 / 倒计时) — not implemented |

## Important

This marketplace plugin **does not** include an `.exe`, system tray, or always-on camera process.

Real capture is the local MCP server: https://github.com/1019666077-bit/webcam_mcp

Requires **Cursor 2.6+** for MCP Apps UI. Homepage: https://mymoying.com/webcam — coming soon.

## Install

1. Install from Cursor Marketplace / Grok Bot Connect Apps (after listing), **or** clone into `~/.cursor/plugins/local/webcam-bridge` and **Reload Window**.
2. Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
3. Point `mcp.json` `--with` at a `webcam_mcp` build that includes `webcam_panel` (local path or git once published).
4. Allow OS camera access for Cursor if asked.
5. Ask for a photo, or run the `snap` command → click **拍一张**.

## What’s inside

| Piece | Role |
| --- | --- |
| `mcp.json` | Starts `webcam_mcp` over stdio via `uv` |
| `scripts/stdio_server.py` | Thin stdio entry |
| `skills/webcam-snap` | Buttons first; image must be visible |
| `rules/webcam-bridge.mdc` | Same playbook, always on |
| `commands/snap` | Open Free panel |
| `commands/check-webcam` | Version / uv / tools check (no camera) |

## License

MIT — see `LICENSE`.

## Author

Moying Studio · moying.studio@outlook.com
