# Sudoku Solver using CSP and Backtracking

## Project overview
This Python project solves a standard 9×9 Sudoku puzzle by modelling it as a **Constraint Satisfaction Problem (CSP)** and searching for a solution using **recursive backtracking**.

### CSP formulation
- **Variables:** Each empty Sudoku cell is a variable.
- **Domains:** Each variable can take values 1 through 9.
- **Constraints:** A digit must not repeat in the same row, column, or 3×3 box.
- **Variable selection:** Minimum Remaining Values (MRV) chooses the empty cell with the fewest legal values first.
- **Backtracking:** If a choice leads to a contradiction, the solver resets the cell and tries another candidate.

## Requirements
- Python 3.9 or later (uses built-in libraries only)
- No external packages required

## Run the project
1. Extract `Sudoku_CSP_Backtracking_Project.zip`.
2. Open a terminal in the extracted folder.
3. Run:
   ```bash
   python3 main.py
   ```
4. Enter `1` to solve the included sample puzzle, or `2` to enter your own puzzle.
5. For a custom puzzle, enter 9 rows. Each row must contain 9 characters; use `0` or `.` for blank cells.

Example row:
```text
530070000
```

## Project files
- `main.py` — complete solver and terminal interface.
- `sample_puzzle.txt` — sample input puzzle.
- `requirements.txt` — no third-party dependencies.
- `PROJECT_REPORT.md` — report with algorithm, design, pseudocode, complexity, and testing.

## Algorithm pseudocode
```text
SOLVE(grid):
    cell = empty cell with the fewest legal candidates (MRV)
    if there is no empty cell:
        return success
    if cell has no candidates:
        return failure
    for each candidate value:
        assign value to cell
        if SOLVE(grid):
            return success
        reset cell to empty
    return failure
```

## Complexity
Let `d` be the maximum domain size (9) and `n` be the number of empty cells. A broad worst-case search bound is O(9^n), with additional time spent checking constraints and selecting variables. MRV typically reduces the search tree substantially, but it does not remove the exponential worst-case nature of backtracking.

## Limitations
- Designed for standard 9×9 Sudoku.
- The solver returns one solution, not every possible solution.
- It checks whether the given clues conflict, but does not separately report whether a puzzle has multiple solutions.
