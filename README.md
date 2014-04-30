# Depth-First Sudoku Solver
Andrew Daws <br />
CS 455-01 <br />
April 30, 2014 <br />

### Description
For centuries Sudoku puzzles have created and attempted to be solved through simple brainstorming. For anyone who is unaware of Sudoku, it is a system of logic heavy, combinatorial number-placement puzzles in which the objective is to fill a 9x9 grid such that each of the nine 3x3 sub-grids, rows, and columns are composed of all digits from 1 to 9 so there are no duplicates. Any generated Sudoku puzzle is composed of a partially filled grid, from which a player is to try and fill the whole puzzle to completion, such that the unique solution is found. As any Sudoku players will tell you, puzzles can vary greatly in complexity, creating wide ranges of completion times. This presents the idea that the optimal method to solve Sudoku puzzles is to instead use the great power of computing which should finish puzzles considerably faster. Unfortunately the problem is still not nullified unless a suitable solving method is established and used, which can require sophisticated strategies with the massive number of possible routes that can be taken at any point, creating an unimaginable number of potential solutions. <br />

### Purpose:
The purpose of this project is to write a program that will make use of some artificial intelligence technique to solve a given problem. Thus through the completion of this project at least one problem solving method will be understood, such that it can be implemented elsewhere. <br />

### Approach
One route that can be taken is to search for the solution through one of multiple possible methods. There are several search algorithms that can be used such as Breadth-First Search (BFS) and greedy search, but in the case of Sudoku the optimal algorithm is Depth-First Search (DFS). <br />
<br />
Depth-First Search involves the algorithm recursively traversing a search tree or graph structure as far as possible along a particular branch before backtracking to a previous untraveled option if it had not reached the target goal along a branch. Thus in the case of Sudoku the DFS algorithm will recursively consider all possible valid values for a square with the currently known valid grid before changing to a new square.
<br />
This allows the algorithm to simplify the search tree each iteration due to the decreasing number of potential values in each square as it further completes any particular set of rows, columns, or 3x3 sub-grids. The algorithm will finish successfully upon finding the correct value for each square that results in the unique solution in which all rows, columns, and 3x3 sub-grids are composed of all values from 1 to 9. <br />

### Included Files:
- README.md
- SodokuSolver.py
- Puzzles folder with puzzle text files [1-25]

### Instructions:
1. Launch SodokuSolver.py
2. The program will ask to select a puzzle number, each number corresponding to the given number text file in the Puzzles folder
3. If a valid puzzle is selected, the program will attempt to solve the given puzzle
4. Upon completion the program will ask to continue and solve another puzzle
