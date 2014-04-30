# Depth-First Sudoku Solver
#
# Name: Andrew Daws
# CS 455-01
# 30 April 2014
#
# Purpose:
# The purpose of this project is to write a program that will make use of some
# artificial intelligence technique to solve a given problem. Thus through the
# completion of this project at least one problem solving method will be
# understood, such that it can be implemented elsewhere.
#
# Approach:
# One route that can be taken is to search for the solution through one of
# multiple possible methods. There are several search algorithms that can be
# used such as Breadth-First Search (BFS) and greedy search, but in the case of
# Sudoku the optimal algorithm is Depth-First Search (DFS). Depth-First Search
# involves the algorithm recursively traversing a search tree or graph structure
# as far as possible along a particular branch before backtracking to a previous
# untraveled option if it had not reached the target goal along a branch. Thus
# in the case of Sudoku the DFS algorithm will recursively consider all possible
# valid values for a square with the currently known valid grid before changing
# to a new square.This allows the algorithm to simplify the search tree each
# iteration due to the decreasing number of potential values in each square as
# it further completes any particular set of rows, columns, or 3x3 sub-grids.The
# algorithm will finish successfully upon finding the correct value for each
# square that results in the unique solution in which all rows, columns, and 3x3
# sub-grids are composed of all values from 1 to 9.

# Obtains all user input and loops the program
def userInput():

# Initialize variables
selectContinue = 'Y'
selectPuzzle = 0

    # User inputs anything other than no
    while(not(selectContinue == 'N' or selectContinue == 'n')):

        # User selects a puzzle
        print "Please select a Sudoku Puzzle. [1-25]: ",
        try:
            selectPuzzle = int(raw_input())
            print " "

            # Proceed with program if valid selection
            if selectPuzzle > 0 and selectPuzzle <= 25:

                # Fill grid list with the selected puzzle
                fillGrid(selectPuzzle)

                # Solve puzzle
                solvePuzzle()

                # Solve another puzzle
                print "Run again? [Y/N]: "
                selectContinue = raw_input()
                print " "

            # Notify of error if invalid selection
            else:
                print "Invalid selection, please try again."
                print " "

        # Exception handling if a non-integer is entered
        except ValueError:
            print "Invalid input, please try again."
            print " "


# Fill the grid solving for with file input
def fillGrid(selectPuzzle):

    # Create the file string for the selected puzzle
    puzzleString = "Puzzles\\" + str(selectPuzzle) + ".txt"

    # Open puzzle input file with read access
    input = open(puzzleString, "r")

    # Read string from input file one character at a time
    for inputIndex, i in enumerate(input.read()):

        # If value is not 0, otherwise ignore
        if (int)(i):

            # Set the index position in the puzzle as a given
            puzzle[inputIndex] = True

            # Set the index position in the grid as a new value
            grid[inputIndex] = (int)(i)

    # Close the input file to prevent a lockup
    input.close()


# Create a list of row sets [Top to Bottom]
def fillRows():

    # Rows 1 - 3
    row.append([ 0,  1,  2,  3,  4,  5,  6,  7,  8])
    row.append([ 9, 10, 11, 12, 13, 14, 15, 16, 17])
    row.append([18, 19, 20, 21, 22, 23, 24, 25, 26])

    # Rows 4 - 6
    row.append([27, 28, 29, 30, 31, 32, 33, 34, 35])
    row.append([36, 37, 38, 39, 40, 41, 42, 43, 44])
    row.append([45, 46, 47, 48, 49, 50, 51, 52, 53])

    # Rows 7 - 9
    row.append([54, 55, 56, 57, 58, 59, 60, 61, 62])
    row.append([63, 64, 65, 66, 67, 68, 69, 70, 71])
    row.append([72, 73, 74, 75, 76, 77, 78, 79, 80])


# Create list of column sets [Left to Right]
def fillColumns():

    # Columns 1 - 3
    column.append([0,  9, 18, 27, 36, 45, 54, 63, 72])
    column.append([1, 10, 19, 28, 37, 46, 55, 64, 73])
    column.append([2, 11, 20, 29, 38, 47, 56, 65, 74])

    # Columns 4 - 6
    column.append([3, 12, 21, 30, 39, 48, 57, 66, 75])
    column.append([4, 13, 22, 31, 40, 49, 58, 67, 76])
    column.append([5, 14, 23, 32, 41, 50, 59, 68, 77])

    # Columns 7 - 9
    column.append([6, 15, 24, 33, 42, 51, 60, 69, 78])
    column.append([7, 16, 25, 34, 43, 52, 61, 70, 79])
    column.append([8, 17, 26, 35, 44, 53, 62, 71, 80])


# Create list of subgrid sets [Top Left to Bottom Right]
def fillSubgrids():

    # Subgrids 1 - 3
    subgrid.append([ 0,  1,  2,  9, 10, 11, 18, 19, 20])
    subgrid.append([ 3,  4,  5, 12, 13, 14, 21, 22, 23])
    subgrid.append([ 6,  7,  8, 15, 16, 17, 24, 25, 26])

    # Subgrids 4 - 6
    subgrid.append([27, 28, 29, 36, 37, 38, 45, 46, 47])
    subgrid.append([30, 31, 32, 39, 40, 41, 48, 49, 50])
    subgrid.append([33, 34, 35, 42, 43, 44, 51, 52, 53])

    # Subgrids 7 - 9
    subgrid.append([54, 55, 56, 63, 64, 65, 72, 73, 74])
    subgrid.append([57, 58, 59, 66, 67, 68, 75, 76, 77])
    subgrid.append([60, 61, 62, 69, 70, 71, 78, 79, 80])


# Displays the current grid values
def displayGrid():

    # Increment through rows
    for i in range(9):

        # Increment through sets of 3 on each row
        for j in range(3):

            # Print each set of 3
            for k in range(3):

                # Store current grid value to avoid duplicate calculations
                gridTempValue = grid[i*9 + (j*(2+1)) + k]

                # Separate sets of 3
                if k == 0 and j > 0:
                    print "|",

                # Convert grid to string values and print
                if gridTempValue > 0:
                    gridString = str(gridTempValue)
                    print gridString,

                # Print empty grid values
                else:
                    print " ",

        # Move to new print row
        print " "

        # Separate subgrids
        if i == 2 or i == 5:
            print "------+-------+------"

    print " "

# Main function, solves sudoku puzzles
def solvePuzzle():

    # Print out puzzle
    print "Uncompleted Puzzle:\n"
    displayGrid()

    # Initialize variables
    i = 0
    backtrack = 0

    # Check all grid positions
    while(i < 81):

        # Check if the grid position is a given in the puzzle
        if puzzle[i]:

            # Move to next grid position
            if not backtrack:
                i = i + 1

            # Move to previous grid position
            else:
                i = i - 1

        # No gridValue in grid position
        else:
            gridValue = grid[i]
            oldGridValue = grid[i]

            # Check if gridValue is already 9
            while(gridValue < 9):

                    # Not 9, increment
                    if (gridValue < 9):
                        gridValue = gridValue + 1

                     # If value is valid, add to grid postition
                    if checkNumber(gridValue, i):
                        grid[i] = gridValue
                        backtrack = 0
                        break

            # Value is 9, reset gridValue
            if (grid[i] == oldGridValue):
                grid[i] = 0
                backtrack = 1

            # gridValue valid, increment to next grid position, restart
            if not backtrack:
                i = i + 1

            # Backtrack to previous grid postition
            else:
                i = i - 1

    # Print out puzzle solution
    print "Solved Puzzle:\n"
    displayGrid()

    # Reset grid and puzzle
    for i in range(81):
        grid[i] = 0
        puzzle[i] = False


# Determine if gridValue is valid if placed on grid
def checkNumber(gridValue, gridPosition):

    # Get current position
    getRow = gridPosition / 9
    getColumn = gridPosition % 9
    getSubgrid = (getRow / 3) * 3 + (getColumn / 3)

    # Check if gridValue is not already in row
    for i in row[getRow]:
        if (grid[i] == gridValue):
            return False

    # Check if gridValue is not already in column
    for i in column[getColumn]:
        if (grid[i] == gridValue):
            return False

    # Check if gridValue is not already in subgrid
    for i in subgrid[getSubgrid]:
        if (grid[i] == gridValue):
            return False

    # Value is valid
    return True


# Create grid list initialized with 0's
grid = [0] * 81

# Create puzzle list initialized with false
puzzle = [False] * 81

# Create empty row list
row = []

# Create empty column list
column = []

# Create empty subgrid list
subgrid = []

# Fill row list
fillRows()

# Fill column list
fillColumns()

# Fill subgrid list
fillSubgrids()

# Initialize user input
userInput()
