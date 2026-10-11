---
name: snap
description: Take one webcam frame into the current conversation and release the camera
---

The user asked for one photo. Call the `webcam` MCP tool `take_photo` once. Describe the returned JPEG in this conversation. Do not call `record_video`. Do not save or upload the image unless they ask. If capture fails, say so and do not invent a frame.
