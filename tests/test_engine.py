from grid import Grid
from engine import GameEngine
from rules import LifeRule


def test_birth_rule():
    grid = Grid(5, 5)
    grid.set(1, 0, 1)
    grid.set(0, 1, 1)
    grid.set(2, 1, 1)

    engine = GameEngine(grid, LifeRule.from_string("23/3"))
    engine.step()

    assert engine.grid.get(1, 1) == 1