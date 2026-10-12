---
name: snap
description: Open Webcam Bridge Free buttons (拍一张 / 再拍 / 关掉); user clicks to put a JPEG in this chat
---

Open the Free webcam panel. Call the `webcam` MCP tool `webcam_panel` once so the chat shows **拍一张 / 再拍 / 关掉**. Do **not** call `take_photo` yourself yet. Tell the user to click **拍一张**; after they do, the JPEG must appear in this conversation and the camera is released. Then describe the visible image. Do not call `record_video`. Do not save or upload unless they ask. Pro buttons are placeholders — ignore them.
