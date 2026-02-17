"""
Application entry point for Conway's Game of Life.

This module initializes the simulation components and runs
the main update loop.

Features:
---------
- User can select rule variant (e.g., 23/3, 16/6, 23/36)
- User can choose grid size, initial density, and simulation speed
- User can insert multiple predefined patterns at chosen coordinates
- Beginner-friendly ASCII pattern examples
- Optional automatic preset for quick start
- CTRL + C stops the simulation safely
"""

from grid import Grid
from engine import GameEngine
from renderer import TerminalRenderer
from patterns import add_glider, add_blinker, add_spaceship, add_pulsar
from rules import LifeRule
import config
from utils import sleep


# ------------------------------------------------------------
# USER CONFIGURATION
# ------------------------------------------------------------

def get_user_configuration():
    """
    Ask the user for simulation parameters.
    Defaults are taken from config.py if the user presses Enter.
    """
    print("\n=== Simulation Setup ===")
    print("Press Enter to use default values.\n")

    rule_input = input(f"Rule variant (default: {config.RULE}) [23/3, 16/6, 23/36]: ").strip()
    rule = rule_input if rule_input else config.RULE

    width_input = input(f"Grid width (default: {config.WIDTH}): ").strip()
    width = int(width_input) if width_input else config.WIDTH

    height_input = input(f"Grid height (default: {config.HEIGHT}): ").strip()
    height = int(height_input) if height_input else config.HEIGHT

    density_input = input(f"Initial life density 0-1 (default: {config.INITIAL_LIFE_PROB}): ").strip()
    density = float(density_input) if density_input else config.INITIAL_LIFE_PROB

    delay_input = input(f"Generation delay in seconds (default: {config.GENERATION_DELAY}): ").strip()
    delay = float(delay_input) if delay_input else config.GENERATION_DELAY

    return {
        "rule": rule,
        "width": width,
        "height": height,
        "density": density,
        "delay": delay
    }


# ------------------------------------------------------------
# BEGINNER-FRIENDLY PATTERN EXAMPLES
# ------------------------------------------------------------

def show_pattern_examples():
    """Display ASCII guides for beginners."""
    print("\n=== Pattern Examples ===")
    print("1. Glider (moves diagonally)")
    print("   *  ")
    print("    *")
    print(" ***")
    print()
    print("2. Blinker (oscillator)")
    print("***")
    print()
    print("3. Lightweight Spaceship (moves horizontally)")
    print("  ***")
    print("*   *")
    print("    *")
    print("*  ")
    print()
    print("4. Pulsar (13x13 oscillator)")
    print("Large 13x13 pattern, oscillates every 3 generations.")
    print("Make sure coordinates leave enough space to fit it!")
    print("========================\n")


def select_patterns(grid):
    """
    Let the user select patterns and their coordinates.
    Modifies grid in-place.
    """
    show_pattern_examples()

    pattern_menu = {
        "1": ("Glider", add_glider),
        "2": ("Blinker", add_blinker),
        "3": ("Lightweight Spaceship", add_spaceship),
        "4": ("Pulsar", add_pulsar)
    }

    print("Select patterns to insert (enter numbers separated by commas).")
    for key, (name, _) in pattern_menu.items():
        print(f"{key}: {name}")
    print("Press Enter to skip pattern insertion and use a preset example.")

    choice = input("Your choice: ").strip()
    if not choice:
        # Optional beginner preset
        add_example_preset(grid)
        return

    choices = [c.strip() for c in choice.split(",")]

    for c in choices:
        if c in pattern_menu:
            name, func = pattern_menu[c]
            try:
                x = int(input(f"Enter X coordinate for {name}: ").strip())
                y = int(input(f"Enter Y coordinate for {name}: ").strip())
                func(grid, x, y)
                print(f"{name} added at ({x},{y})")
            except ValueError:
                print("Invalid coordinates, skipping this pattern.")


def add_example_preset(grid):
    """
    Add a beginner-friendly preset of multiple patterns.
    """
    add_glider(grid, 5, 5)
    add_blinker(grid, 10, 10)
    add_spaceship(grid, 20, 5)
    print("Automatic example patterns added to the grid.")


# ------------------------------------------------------------
# SIMULATION INITIALIZATION
# ------------------------------------------------------------

def initialize_simulation(settings):
    """
    Create and configure simulation components.
    """
    grid = Grid(settings["width"], settings["height"])
    grid.randomize(settings["density"])

    # Let user place patterns
    select_patterns(grid)

    # Load Life rule
    rule = LifeRule.from_string(settings["rule"])

    # Initialize engine and renderer
    engine = GameEngine(grid, rule)
    renderer = TerminalRenderer()

    return engine, renderer


# ------------------------------------------------------------
# USER INFO DISPLAY
# ------------------------------------------------------------

def print_startup_info(settings):
    """
    Display simulation configuration and instructions.
    """
    print("\nConway's Game of Life — Terminal Simulation")
    print("-" * 45)
    print(f"Grid size: {settings['width']} x {settings['height']}")
    print(f"Rule: {settings['rule']}")
    print(f"Initial density: {settings['density']}")
    print(f"Generation delay: {settings['delay']} seconds")
    print("You can insert patterns at chosen coordinates.")
    print("Press CTRL + C to stop the simulation.\n")


# ------------------------------------------------------------
# MAIN LOOP
# ------------------------------------------------------------

def main():
    """Run the Game of Life simulation."""
    settings = get_user_configuration()
    print_startup_info(settings)
    engine, renderer = initialize_simulation(settings)

    generation = 0

    try:
        while True:
            renderer.draw(engine.grid, generation)
            # Always display CTRL+C stop message below grid
            print("Press CTRL + C to stop the simulation.\n")
            engine.step()
            generation += 1
            sleep(settings["delay"])

    except KeyboardInterrupt:
        print("\nSimulation stopped.")

if __name__ == "__main__":
    main()