"""
Global configuration for the Game of Life simulation.

Centralizes all runtime parameters to avoid hard-coded values.
Modify this file to change simulation behavior.
"""

# ===============================
# GRID CONFIGURATION
# ===============================

WIDTH = 80
HEIGHT = 30

# Probability of a cell being alive at initialization
INITIAL_LIFE_PROB = 0.25

# Delay between generations (seconds)
GENERATION_DELAY = 0.08

# ===============================
# RENDERING CONFIGURATION
# ===============================

ALIVE_CHAR = "█"
DEAD_CHAR = " "

# ===============================
# LIFE RULE CONFIGURATION
# ===============================

# Format: SURVIVAL/BIRTH
# Example:
# "23/3"   -> Standard Conway Life
# "23/36"  -> HighLife
# "16/6"   -> Custom rule

RULE = "23/3"