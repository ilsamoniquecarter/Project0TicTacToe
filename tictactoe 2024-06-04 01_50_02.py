"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    def player(board):
        def is_terminal(board):
            # Check rows
            for row in board:
                if row[0] == row[1] == row[2] and row[0] != ' ':
                    return True
        # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
                return True
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
            return True
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
            return True
        # Check for a draw (no empty spaces)
        if all(cell != ' ' for row in board for cell in row):
            return True
        return False

    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)

    # Check if the board is in a terminal state
    if in a terminal state(board):
        return "Game over"

    if x_count == o_count:
        return 'X'
    elif x_count == o_count + 1:
        return 'O'
    else:
        raise ValueError("Invalid board state")

# Example usage
board = [
    ['X', 'O', 'X'],
    [' ', 'X', ' '],
    ['O', ' ', ' ']
]

print(player(board))  # Output: 'O'



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    def actions(board):
        """
        Returns a set of all possible actions (i, j) available on the board.
        Each action corresponds to an empty cell.
        """
        possible_actions = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ' ':
                    possible_actions.add((i, j));return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    The original board is not modified; a new board is returned.
    Raises an exception if the action is invalid.
    """
    i, j = action
    if board[i][j] != ' ':
        raise ValueError("Invalid action: Cell is not empty.")

    # Deep copy the board
    new_board = [row[:] for row in board]

    # Get the current player
    current_player = 'X' if sum(row.count('X') for row in board) == sum(row.count('O') for row in board) else 'O'

    # Apply the action
    new_board[i][j] = current_player

    return new_board

# Example usage
board = [
    ['X', 'O', 'X'],
    [' ', 'X', ' '],
    ['O', ' ', ' ']
]

print(actions(board))  # Output: {(1, 0), (1, 2), (2, 1), (2, 2)}

new_board = result(board, (1, 0))
for row in new_board:
    print(row)
# Output:
# ['X', 'O', 'X']
# ['X', 'X', ' ']
# ['O', ' ', ' ']


print(actions(board))  # Output: {(1, 0), (1, 2), (2, 1), (2, 2)}


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    def winner(board):
        """
    Returns the winner of the game, if there is one.
    """
    # Check rows for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    # If no winner, return None
    return None

# Example usage
board1 = [
    ['X', 'O', 'X'],
    [' ', 'X', ' '],
    ['O', ' ', 'X']
]

board2 = [
    ['X', 'O', 'X'],
    ['O', 'O', 'O'],
    ['X', ' ', ' ']
]

board3 = [
    ['X', 'O', 'X'],
    [' ', 'X', ' '],
    ['O', ' ', ' ']
]

print(winner(board1))  # Output: X (X wins diagonally)
print(winner(board2))  # Output: O (O wins horizontally)
print(winner(board3))  # Output: None (No winner yet)



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    def terminal(board):
        """
    Returns True if the game is over, False otherwise.
    """
    # Check if there's a winner
    if winner(board) is not None:
        return True

    # Check if all cells are filled
    for row in board:
        if ' ' in row:
            return False

    # If no winner and no empty cells, the game is over
    return True

# Example usage
board1 = [
    ['X', 'O', 'X'],
    [' ', 'X', ' '],
    ['O', ' ', 'X']
]

board2 = [
    ['X', 'O', 'X'],
    ['O', 'O', 'O'],
    ['X', ' ', ' ']
]

board3 = [
    ['X', 'O', 'X'],
    ['X', 'O', 'X'],
    ['O', 'X', 'O']
]

board4 = [
    ['X', 'O', 'X'],
    [' ', 'X', ' '],
    ['O', ' ', ' ']
]

print(terminal(board1))  # Output: True (X wins diagonally)
print(terminal(board2))  # Output: True (O wins horizontally)
print(terminal(board3))  # Output: True (All cells filled, no winner)
print(terminal(board4))  # Output: False (Game still in progress)



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    def utility(board):
        """
    Returns the utility of the board:
    - 1 if X has won
    - -1 if O has won
    - 0 if the game is a tie
    """
    win = winner(board)
    if win == 'X':
        return 1
    elif win == 'O':
        return -1
    else:
        return 0

# Example usage
board1 = [
    ['X', 'O', 'X'],
    [' ', 'X', ' '],
    ['O', ' ', 'X']
]

board2 = [
    ['X', 'O', 'X'],
    ['O', 'O', 'O'],
    ['X', ' ', ' ']
]

board3 = [
    ['X', 'O', 'X'],
    ['X', 'O', 'X'],
    ['O', 'X', 'O']
]

print(utility(board1))  # Output: 1 (X wins)
print(utility(board2))  # Output: -1 (O wins)
print(utility(board3))  # Output: 0 (Tie)



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == 'X':
        _, move = max_value(board)
    else:
        _, move = min_value(board)

    return move
def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    optimal_move = None
    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > v:
            v = min_val
            optimal_move = action

    return v, optimal_move

def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    optimal_move = None
    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < v:
            v = max_val
            optimal_move = action

    return v, optimal_move
