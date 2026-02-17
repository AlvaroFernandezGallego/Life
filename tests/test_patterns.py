from grid import Grid
from patterns import add_glider


def test_glider():
    grid = Grid(10, 10)
    add_glider(grid, 1, 1)

    assert grid.get(2, 1) == 1
