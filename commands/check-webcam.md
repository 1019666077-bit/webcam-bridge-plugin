---
name: check-webcam
description: Check that uv can import the local webcam_mcp server without opening the camera
---

Check that `uv` is on PATH. Then run:

```bash
uv run --no-project --with git+https://github.com/1019666077-bit/webcam_mcp python -c "import webcam_mcp; print(webcam_mcp.__version__)"
```

Do not open the camera and do not call `take_photo` unless the user also asked for a frame.

If `uv` is missing, point them to https://docs.astral.sh/uv/getting-started/installation/. This plugin has no exe and no tray. The homepage https://mymoying.com/webcam is coming soon. Real capture is https://github.com/1019666077-bit/webcam_mcp.
