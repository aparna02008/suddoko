"""
Sudoku Solver using Constraint Satisfaction Problem (CSP) and Backtracking
Run: python3 main.py
"""
from typing import List, Optional, Tuple

Grid = List[List[int]]
SIZE = 9
DIGITS = set(range(1, 10))


def print_grid(grid: Grid) -> None:
    """Print a Sudoku grid in a readable 9x9 format."""
    for r in range(SIZE):
        if r % 3 == 0 and r != 0:
            print("-" * 21)
        row = []
        for c in range(SIZE):
            if c % 3 == 0 and c != 0:
                row.append("|")
            row.append(str(grid[r][c]) if grid[r][c] != 0 else ".")
        print(" ".join(row))


def is_valid_value(grid: Grid, row: int, col: int, value: int) -> bool:
    """Check the CSP constraints for placing value at (row, col)."""
    if any(grid[row][c] == value for c in range(SIZE)):
        return False
    if any(grid[r][col] == value for r in range(SIZE)):
        return False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if grid[r][c] == value:
                return False
    return True


def find_empty_cell(grid: Grid) -> Optional[Tuple[int, int]]:
    """Find the next unassigned variable (empty cell)."""
    for r in range(SIZE):
        for c in range(SIZE):
            if grid[r][c] == 0:
                return r, c
    return None


def candidates_for(grid: Grid, row: int, col: int) -> set[int]:
    """Return the domain of legal values for an empty cell."""
    used = set(grid[row])
    used.update(grid[r][col] for r in range(SIZE))
    br, bc = (row // 3) * 3, (col // 3) * 3
    used.update(grid[r][c] for r in range(br, br + 3)
                for c in range(bc, bc + 3))
    return DIGITS - used


def find_mrv_cell(grid: Grid) -> Optional[Tuple[int, int, set[int]]]:
    """
    Minimum Remaining Values (MRV) heuristic:
    choose the empty cell with the fewest legal candidates.
    """
    best = None
    best_candidates = None
    for r in range(SIZE):
        for c in range(SIZE):
            if grid[r][c] == 0:
                candidates = candidates_for(grid, r, c)
                if best is None or len(candidates) < len(best_candidates):
                    best = (r, c)
                    best_candidates = candidates
                if not candidates:
                    return r, c, set()
    if best is None:
        return None
    return best[0], best[1], best_candidates


def solve_sudoku(grid: Grid) -> bool:
    """Solve the puzzle using recursive backtracking and MRV."""
    selected = find_mrv_cell(grid)
    if selected is None:
        return True  # No empty cells remain.

    row, col, candidates = selected
    if not candidates:
        return False  # Dead end: backtrack.

    for value in sorted(candidates):
        if is_valid_value(grid, row, col, value):
            grid[row][col] = value
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0  # Undo choice and backtrack.
    return False


def validate_grid(grid: Grid) -> bool:
    """Validate dimensions, values, and initial Sudoku constraints."""
    if len(grid) != SIZE or any(len(row) != SIZE for row in grid):
        return False
    for r in range(SIZE):
        for c in range(SIZE):
            value = grid[r][c]
            if not isinstance(value, int) or value not in range(10):
                return False
            if value != 0:
                grid[r][c] = 0
                valid = is_valid_value(grid, r, c, value)
                grid[r][c] = value
                if not valid:
                    return False
    return True


def read_puzzle() -> Grid:
    """Read 9 lines; use 0 or . for blank cells."""
    print("Enter 9 rows of 9 digits.")
    print("Use 0 or . for empty cells. Example: 530070000")
    grid = []
    for i in range(SIZE):
        while True:
            line = input(f"Row {i + 1}: ").strip().replace(" ", "")
            if len(line) == SIZE and all(ch in "0123456789." for ch in line):
                grid.append([0 if ch == "." else int(ch) for ch in line])
                break
            print("Invalid row. Please enter exactly 9 digits (0 or . for blanks).")
    return grid


def main() -> None:
    print("=" * 43)
    print("       SUDOKU SOLVER: CSP + BACKTRACKING")
    print("=" * 43)
    print("1. Solve the sample puzzle")
    print("2. Enter your own puzzle")
    choice = input("Choose (1/2): ").strip()

    sample = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    grid = sample if choice == "1" else read_puzzle()

    if not validate_grid(grid):
        print("\nThe puzzle has conflicting or invalid starting values.")
        return

    print("\nInput puzzle:")
    print_grid(grid)
    print("\nSolving...")
    if solve_sudoku(grid):
        print("\nSolved puzzle:")
        print_grid(grid)
    else:
        print("\nNo solution exists for this puzzle.")


if __name__ == "__main__":
    main()
