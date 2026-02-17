"""
Launcher script for Conway's Game of Life.

This script opens a NEW terminal tab/window and runs the game.
This ensures proper rendering and interaction with the simulation.

Cross-platform support:
- Linux (gnome-terminal / xterm)
- macOS (Terminal.app)
- Windows (cmd)
"""

import os
import sys
import subprocess
import platform


def open_new_terminal():
    """
    Open a new terminal window/tab and execute main.py.

    The implementation depends on the operating system.
    """

    system = platform.system()

    # ---------- Linux ----------
    if system == "Linux":
        try:
            # Try GNOME terminal first (most common)
            subprocess.Popen(
                ["gnome-terminal", "--", "python3", "main.py"]
            )
        except FileNotFoundError:
            # Fallback to xterm
            subprocess.Popen(
                ["xterm", "-e", "python3 main.py"]
            )

    # ---------- macOS ----------
    elif system == "Darwin":
        subprocess.Popen(
            [
                "osascript",
                "-e",
                'tell app "Terminal" to do script "python3 main.py"'
            ]
        )

    # ---------- Windows ----------
    elif system == "Windows":
        subprocess.Popen(
            ["start", "cmd", "/k", "python main.py"],
            shell=True
        )

    else:
        print("Unsupported operating system.")


if __name__ == "__main__":
    open_new_terminal()
