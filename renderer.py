"""
Terminal renderer module.

Handles visualization of the simulation.
"""

import os
from config import ALIVE_CHAR, DEAD_CHAR


class TerminalRenderer:
    """Renders grid in terminal."""

    def clear(self):
        """Clear terminal screen."""
        os.system("cls" if os.name == "nt" else "clear")

    def draw(self, grid, generation: int):
        """
        Render simulation state.

        Args:
            grid: Grid to display.
            generation: Current generation number.
        """
        self.clear()

        print("╔" + "═" * grid.width + "╗")
        print(f"║ Generation: {generation}".ljust(grid.width + 1) + "║")
        print("╠" + "═" * grid.width + "╣")

        for y in range(grid.height):
            row = "".join(
                ALIVE_CHAR if grid.get(x, y) else DEAD_CHAR
                for x in range(grid.width)
            )
            print("║" + row + "║")

        print("╚" + "═" * grid.width + "╝")
