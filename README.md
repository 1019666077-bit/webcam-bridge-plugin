# Webcam Bridge (Cursor plugin)

**Free, MIT.** On-demand one frame from the local webcam. The camera is released when the shot finishes. The JPEG comes back into the current conversation.

## Important

This marketplace plugin **does not** include:

- An `.exe` installer
- A system tray app
- An always-on camera process

Real capture is the local MCP server: https://github.com/1019666077-bit/webcam_mcp

`take_photo` opens the camera, returns one JPEG, and releases the device before the tool returns. That image is the picture in the current chat.

Homepage: https://mymoying.com/webcam — coming soon.

## Install

1. Install from Cursor Marketplace (after listing), **or** clone into `~/.cursor/plugins/local/webcam-bridge` and reload.
2. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) so Cursor can start the server from that Git repo.
3. Allow camera access for Cursor if the operating system asks.
4. Ask for one photo, or run the `snap` command.

The first start needs network access so `uv` can fetch `webcam_mcp`. The camera stays closed until `take_photo` runs. This bridge uses camera index `0`.

## What’s inside

| Piece | Role |
| --- | --- |
| `mcp.json` | Starts `webcam_mcp` over stdio via `uv` (no bundled server, no exe) |
| `scripts/stdio_server.py` | Thin stdio entry. Capture and release stay in `webcam_mcp` |
| `skills/webcam-snap` | When to take one frame, and how the image returns to this chat |
| `rules/webcam-bridge.mdc` | On demand only; release after the shot; no tray |
| `commands/snap` | Take one frame into this conversation |
| `commands/check-webcam` | Check `uv` and that `webcam_mcp` imports, without opening the camera |

`webcam_mcp` also exposes `record_video`. This plugin’s playbook does not use it: one still frame, then the camera is released.

## License

MIT — see `LICENSE`.

## Author

Moying Studio · moying.studio@outlook.com
