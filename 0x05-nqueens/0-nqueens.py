#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys

solutions = []
"""The list of possible solutions to the N queens problem.
"""
n = 0
"""The size of the chessboard.
"""
pos = None
"""The list of possible positions on the chessboard.
"""

def get_input():
    """Retrives and validates this program's argument.
    Returns:
        int: The size of the chessboard.
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def is_attacking(pos0, pos1):
    """Checks if the position of two queens are in an attacking mode
    Args:
        pos0 (list or tuple): The position of the first queen.
        pos1 (list or tuple): The position of the second queen.
    Returns:
        bool: True if the queens are attacking, False otherwise.
    """
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])

def group_exists(group):
    """Checks if a group of queens exists in a solution.
    Args:
        group (list of integers): A group of possible positions.
    Returns:
        bool: True if it exists, otherwise False.
    """
    global solutions
    for stn in solutions:
        i = 0
        for stn_pos in stn:
            for grp_pos in group:
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    i += 1
        if i == n:
            return True
    return False

def get_solutions():
    """Gets the solutions for the given chessboard size.
    """
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n * n)))
    a = 0
    group = [[]]  # Start with an empty position in the group
    build_solution(0, group)

def build_solution(row, valid_positions):
    """Builds a solution for the n queen problem.
    Args:
        row (int): The current row in the chessboard.
        valid_positions (list of lists of integers): The list of valid positions for queens.
    """
    global solutions
    global n
    if row == n:
        tmp0 = valid_positions.copy()
        if not group_exists(tmp0):  # Use valid_positions for checking existence
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            new_position = pos[a].copy()
            if valid_positions:  # Check if valid_positions is not empty
                matches = zip(list([new_position]) * len(valid_positions), valid_positions)
                used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            else:
                matches = []
                used_positions = []
            # Append to valid_positions instead of group
            valid_positions.append(new_position)
            if not any(used_positions):
                build_solution(row + 1, valid_positions.copy())  # Pass a copy on recursion
            # Remove from valid_positions after checking the sub-tree
            valid_positions.pop()


def get_solutions():
    """Gets the solutions for the given chessboard size.
    """
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n * 2)))
    a = 0
    group = []
    build_solution(0, group)

n = get_input()
get_solutions()
for solutions in solutions:
    print(solutions)