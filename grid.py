"""
Grid module.

Defines the Grid class representing the 2D cellular space.
Handles storage, access, bounds checking, and cloning.
"""

import random


class Grid:
    """
    Represents a 2D grid of cells.

    Each cell is:
        1 -> alive
        0 -> dead
    """

    def __init__(self, width: int, height: int):
        """
        Initialize empty grid.

        Args:
            width: Number of columns.
            height: Number of rows.
        """
        self.width = width
        self.height = height

        # Create 2D matrix initialized to dead cells
        self.cells = [
            [0 for _ in range(width)]
            for _ in range(height)
        ]

    def randomize(self, probability: float) -> None:
        """
        Randomly populate grid.

        Args:
            probability: Probability of a cell being alive.
        """
        for y in range(self.height):
            for x in range(self.width):
                self.cells[y][x] = 1 if random.random() < probability else 0

    def get(self, x: int, y: int) -> int:
        """Return state of a cell."""
        return self.cells[y][x]

    def set(self, x: int, y: int, value: int) -> None:
        """Set state of a cell."""
        self.cells[y][x] = value

    def in_bounds(self, x: int, y: int) -> bool:
        """Check if coordinates are inside grid."""
        return 0 <= x < self.width and 0 <= y < self.height

    def copy(self):
        """
        Create deep copy of grid.

        Returns:
            New Grid instance.
        """
        new_grid = Grid(self.width, self.height)
        new_grid.cells = [row[:] for row in self.cells]
        return new_grid
