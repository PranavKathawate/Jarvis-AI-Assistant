import pystray
from pystray import MenuItem as item
from PIL import Image
import threading
import sys
import os
import jarvis_main


def run_jarvis():
    jarvis_main.start_jarvis()


def on_exit(icon, item):
    icon.stop()
    sys.exit()


# ✅ Proper resource path handler for PyInstaller
def resource_path(relative_path):
    """
    Get absolute path to resource,
    works for dev and for PyInstaller onefile exe
    """
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# Load tray icon safely
icon_path = resource_path("icon.png")
image = Image.open(icon_path)

# Create tray icon
icon = pystray.Icon(
    "Jarvis",
    image,
    "Jarvis Assistant",
    menu=pystray.Menu(
        item("Exit", on_exit)
    )
)

# Start Jarvis in background thread
threading.Thread(target=run_jarvis, daemon=True).start()

# Run tray system
icon.run()