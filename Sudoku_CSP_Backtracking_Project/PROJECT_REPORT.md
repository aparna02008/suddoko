# Sudoku Solver Using Constraint Satisfaction Problem (CSP) and Backtracking

## 1. Abstract
Sudoku is a number-placement puzzle in which every row, every column, and every 3×3 subgrid must contain the digits 1 to 9 without repetition. This project implements a Sudoku solver using Artificial Intelligence concepts. It models the puzzle as a Constraint Satisfaction Problem (CSP) and uses recursive backtracking to find a valid solution. The Minimum Remaining Values (MRV) heuristic selects the next empty cell with the fewest legal candidate values, helping the search reach contradictions earlier and reducing unnecessary exploration.

## 2. Introduction
A Constraint Satisfaction Problem consists of variables, domains, and constraints. Sudoku naturally fits this model: cells are variables, digits 1–9 are domains, and row, column, and box rules are constraints. The program accepts a built-in example or a puzzle entered by the user, validates the initial clues, and prints a solved grid when a solution exists.

## 3. Objectives
- Apply CSP concepts to a familiar puzzle.
- Implement recursive backtracking.
- Enforce row, column, and 3×3 box constraints.
- Use MRV to choose a promising variable.
- Accept user-provided puzzles and handle invalid or unsolvable inputs.

## 4. Problem statement
Given a partially completed 9×9 Sudoku grid, fill every blank cell with a digit from 1 to 9 so that each row, each column, and each 3×3 box contains no repeated digit. If no valid completion exists, report that no solution was found.

## 5. System requirements
**Software:** Python 3.9+, terminal or command prompt, any text editor or IDE.  
**Hardware:** A standard computer capable of running Python.  
**Dependencies:** No third-party packages.

## 6. CSP formulation
### Variables
Each cell `X[r][c]` is a variable. Given clues are fixed; empty cells are unassigned variables.

### Domains
For an empty cell, the initial domain is `{1,2,3,4,5,6,7,8,9}`. Its legal domain is reduced by digits already present in the same row, column, and box.

### Constraints
1. **Row constraint:** No digit occurs more than once in a row.
2. **Column constraint:** No digit occurs more than once in a column.
3. **Box constraint:** No digit occurs more than once in a 3×3 box.

These are all-different constraints for each row, column, and box.

## 7. Methodology
1. Read a sample puzzle or a custom 9×9 grid.
2. Check dimensions, digit ranges, and conflicts among the starting clues.
3. Find an empty cell using the Minimum Remaining Values heuristic.
4. Calculate the legal candidate values for that cell.
5. Try each candidate in sorted order.
6. Recursively attempt to solve the updated grid.
7. If a branch fails, reset the cell to zero and try the next candidate.
8. If no empty cells remain, report success and print the solution.

## 8. Algorithm
```text
BACKTRACK(grid):
    cell ← empty cell with minimum legal candidates (MRV)
    if no empty cell exists:
        return TRUE
    if cell has zero legal candidates:
        return FALSE
    for each value in cell's legal candidates:
        assign value to cell
        if BACKTRACK(grid) is TRUE:
            return TRUE
        reset cell to empty
    return FALSE
```

## 9. Module description
- `print_grid`: prints the grid with visual separators.
- `is_valid_value`: checks row, column, and box rules.
- `candidates_for`: computes legal values for an empty cell.
- `find_mrv_cell`: chooses the unassigned variable with the smallest remaining domain.
- `solve_sudoku`: performs recursive backtracking and restores failed assignments.
- `validate_grid`: checks the puzzle dimensions, allowed values, and conflicting clues.
- `read_puzzle`: collects nine valid rows from the user.
- `main`: provides the menu, invokes validation and solving, and displays the result.

## 10. Sample input
```text
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079
```
A zero represents an empty cell.

## 11. Expected output
The solved grid for the included sample is:
```text
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
---------------------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
---------------------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```

## 12. Testing
| Test case | Input | Expected result |
|---|---|---|
| 1 | Included valid sample | Displays a completed valid grid |
| 2 | Valid custom puzzle | Attempts to solve and displays a solution if one exists |
| 3 | Duplicate starting clues in a row, column, or box | Reports conflicting starting values |
| 4 | Valid but unsolvable puzzle | Reports that no solution exists |
| 5 | Invalid row length or characters | Requests the row again |

## 13. Complexity analysis
If `n` cells are empty and each cell has at most nine possible values, a loose worst-case search bound is `O(9^n)`. Candidate checks and MRV selection add overhead per recursive call. MRV often reduces the practical search significantly by selecting the most constrained cell first. The worst-case complexity remains exponential.

## 14. Advantages
- Demonstrates AI search and CSP clearly.
- Uses only Python's standard library.
- Checks input conflicts before search.
- MRV can reduce unnecessary exploration.
- Includes both a sample puzzle and custom input mode.

## 15. Limitations and future enhancements
The program returns one solution and does not count all solutions. Future improvements could include a graphical interface, step-by-step visualization, forward checking, arc consistency (AC-3), puzzle generation, and multiple-solution detection.

## 16. Conclusion
The project demonstrates how Sudoku can be formulated as a CSP and solved through backtracking. Row, column, and box constraints ensure correctness, while MRV improves variable selection. The result is a compact, dependency-free educational implementation of an AI problem-solving technique.
