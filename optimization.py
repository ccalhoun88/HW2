# optimization.py
# ---------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to Kansas State University CS 530/730.

import random

def count_conflicts(board):
    """
    Counts the number of pairs of queens that attack each other.
    Board representation: A list where index i is the column, and board[i] is the row.
    Example: [0, 1, 2, 3] means queens are on the diagonal (max conflicts).
    """
    N = len(board)
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            # Check same row
            if board[i] == board[j]:
                conflicts += 1
            # Check diagonal
            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def get_all_neighbors(board):
    """
    Returns a list of all possible neighbors (moving one queen to a new row).
    Returns tuples of (new_board, conflict_count).
    """
    neighbors = []
    N = len(board)
    for col in range(N):
        original_row = board[col]
        for new_row in range(N):
            if new_row != original_row:
                new_board = list(board)
                new_board[col] = new_row
                neighbors.append((new_board, count_conflicts(new_board)))
    return neighbors

def random_board(n):
    """Returns a random board of size n."""
    return [random.randint(0, n - 1) for _ in range(n)]

def randomRestartHillClimbing(n):
    """
    Implement Random Restart Hill Climbing to solve the N-Queens problem.
    
    Algorithm:
    1. Start with a random board.
    2. Check neighbors. Move to the neighbor with the lowest conflicts.
    3. If no neighbor is better than current (local minima/plateau):
       - If conflicts == 0, return the board (Solution Found!).
       - Else, RESTART with a new random board.
    """
    "*** YOUR CODE HERE ***"
    return []

if __name__ == '__main__':
    # Test Script
    print("Solving 8-Queens...")
    solution = randomRestartHillClimbing(8)
    print("Solution found:", solution)
    print("Conflicts:", count_conflicts(solution))