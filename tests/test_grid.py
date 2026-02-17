from grid import Grid


def test_grid_initialization():
    grid = Grid(3, 3)
    assert grid.get(1, 1) == 0


def test_set_and_get():
    grid = Grid(3, 3)
    grid.set(1, 1, 1)
    assert grid.get(1, 1) == 1


def test_copy_independent():
    grid = Grid(3, 3)
    grid.set(1, 1, 1)

    clone = grid.copy()
    clone.set(1, 1, 0)

    assert grid.get(1, 1) == 1