---
name: webcam-snap
description: Take one local webcam frame into the current conversation. Use when the user asks for a photo, a snapshot, or to look through the webcam. Capture only on request, then the camera is released.
---

# Webcam snap

## What this is

Webcam Bridge asks the local [webcam_mcp](https://github.com/1019666077-bit/webcam_mcp) server for **one frame**. `take_photo` opens the camera, drops a few warm-up reads, returns one JPEG, and **always releases the device** (`cap.release()` in a `finally` block), including when capture fails.

That JPEG is an MCP image block in **this conversation**. Describe it here. Do not upload it, and do not write it to disk unless the user asks.

This plugin does **not** include an `.exe` or a system tray. There is no always-on camera process. Homepage (coming soon): https://mymoying.com/webcam

## When to shoot

Call the `webcam` MCP tool `take_photo` only after the user asks for a photo in this conversation. One call is one frame. Do not call `record_video`.

If the user did not ask to be photographed, do not open the camera.

## If the tool is missing or fails

- `uv` is required. Install it from https://docs.astral.sh/uv/getting-started/installation/ and reload the plugin. There is no exe to download; the homepage is coming soon.
- Camera errors come from webcam_mcp. Relay them: grant the OS camera permission to Cursor, close other apps using the camera, and note that this bridge uses camera index `0`.
- Do not invent a photo. Say that no frame was captured.

## Completion

Tell the user the frame is the image in this chat, and that the camera was released when the shot finished.
