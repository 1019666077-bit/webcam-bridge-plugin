"""Start the local webcam_mcp server over stdio.

This plugin does not capture pixels, ship an exe, or run a tray app.
Opening the camera, encoding one JPEG, and releasing the device are
implemented in https://github.com/1019666077-bit/webcam_mcp.
"""

from webcam_mcp.config import ServerConfig
from webcam_mcp.server import create_server


def main() -> None:
    create_server(ServerConfig()).run(transport="stdio")


if __name__ == "__main__":
    main()
