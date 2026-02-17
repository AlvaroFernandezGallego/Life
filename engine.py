"""
Game engine module.

Implements simulation logic using configurable Life rules.
Contains no rendering logic.
"""


class GameEngine:
    """
    Controls simulation updates.
    """

    def __init__(self, grid, rule):
        """
        Initialize engine.

        Args:
            grid: Grid instance.
            rule: LifeRule instance.
        """
        self.grid = grid
        self.rule = rule

    def count_neighbors(self, x: int, y: int) -> int:
        """Count living neighbors of a cell."""
        neighbors = 0

        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue

                nx = x + dx
                ny = y + dy

                if self.grid.in_bounds(nx, ny):
                    neighbors += self.grid.get(nx, ny)

        return neighbors

    def step(self):
        """
        Compute next generation.

        Returns:
            Updated grid.
        """
        new_grid = self.grid.copy()

        for y in range(self.grid.height):
            for x in range(self.grid.width):
                alive = self.grid.get(x, y)
                neighbors = self.count_neighbors(x, y)

                if alive:
                    if not self.rule.should_survive(neighbors):
                        new_grid.set(x, y, 0)
                else:
                    if self.rule.should_be_born(neighbors):
                        new_grid.set(x, y, 1)

        self.grid = new_grid
        return self.grid
