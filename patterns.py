"""
Pattern library.

Provides reusable patterns for Conway's Game of Life.
Coordinates are relative to top-left insertion point.
"""

def add_glider(grid, x: int, y: int):
    """Insert a glider."""
    coords = [(1,0),(2,1),(0,2),(1,2),(2,2)]
    for dx, dy in coords:
        if grid.in_bounds(x+dx, y+dy):
            grid.set(x+dx, y+dy, 1)

def add_blinker(grid, x: int, y: int):
    """Insert a blinker oscillator."""
    for dx in (-1,0,1):
        if grid.in_bounds(x+dx, y):
            grid.set(x+dx, y, 1)

def add_spaceship(grid, x: int, y: int):
    """Insert a lightweight spaceship."""
    coords = [(1,0),(2,0),(3,0),(0,1),(3,1),(3,2),(0,3),(2,3)]
    for dx, dy in coords:
        if grid.in_bounds(x+dx, y+dy):
            grid.set(x+dx, y+dy, 1)

def add_pulsar(grid, x: int, y: int):
    """Insert a pulsar oscillator (13x13 area)."""
    pattern = [
        "  ***   ***  ",
        "             ",
        "*    * *    *",
        "*    * *    *",
        "*    * *    *",
        "  ***   ***  ",
        "             ",
        "  ***   ***  ",
        "*    * *    *",
        "*    * *    *",
        "*    * *    *",
        "             ",
        "  ***   ***  "
    ]
    for dy, row in enumerate(pattern):
        for dx, char in enumerate(row):
            if char == "*" and grid.in_bounds(x+dx, y+dy):
                grid.set(x+dx, y+dy, 1)