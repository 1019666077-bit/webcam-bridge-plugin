---
name: check-webcam
description: Check Cursor version (2.6+), uv, and that webcam_mcp exposes webcam_panel without opening the camera
---

1. Note Cursor version (Help → About, or `package.json` under the Cursor install). MCP Apps buttons need **2.6+**.
2. Check that `uv` is on PATH.
3. Run:

```bash
uv run --no-project --with "git+https://github.com/1019666077-bit/webcam_mcp@v0.2.0" python -c "from webcam_mcp import __version__; from webcam_mcp.server import create_server; from webcam_mcp.config import ServerConfig; import asyncio; print('webcam_mcp', __version__); s=create_server(ServerConfig()); print([t.name for t in asyncio.run(s.list_tools())])"
```

Expect tools including `webcam_panel`, `take_photo`. Do not open the camera and do not call `take_photo` unless the user also asked for a frame.

If `uv` is missing: https://docs.astral.sh/uv/getting-started/installation/. No exe, no tray. Real capture: https://github.com/1019666077-bit/webcam_mcp
