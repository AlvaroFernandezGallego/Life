# Life

A **terminal-based Python simulation** of Conway's Game of Life
This project allows users to explore cellular automata with customizable rules, grid size, initial density, speed, and interactive patterns

---

## Running the Game

### 1. Using `main.py`

- Runs the simulation **directly in the current terminal window**
- Launch with:

```bash
python main.py
```

### 2. Using `launcher.py`

- Opens the simulation in a new terminal tab or window, keeping your current terminal free
- Launch with:

```bash
python launcher.py
```

## Simulation Setup

When you start the simulation, you can customize:

- **Rule variant**: e.g., `23/3` (standard Conway), `16/6`, `23/36` (HighLife)  
- **Grid width and height**  
- **Initial life density**: 0.0–1.0  
- **Generation delay**: seconds between updates  

### Pattern Selection

- Predefined patterns: **Glider**, **Blinker**, **Lightweight Spaceship**, **Pulsar**  
- You can insert **multiple patterns** at chosen coordinates  
- Press **Enter** to skip pattern selection and use the **automatic beginner preset**  
- **Examples** are displayed to help visualize each pattern  

### Controls

- **CTRL + C** → Stop the simulation at any time  

## Running Unit Tests

- Unit tests are implemented using **pytest**. To run all tests:

```bash
python -m pytest
```

- Recommended to run after modifying rules or patterns to ensure correctness

Enjoy experimenting with **Conway's Game of Life** and exploring how simple rules create complex patterns!  

> Note: This project will receive **updates over time**
