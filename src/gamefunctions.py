# from IPython.display import clear_output
import random

# Display the Tic Tac Toe board
def display_board(board):
    print(' ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] + ' ')
    print('--- | --- | ---')
    print(' ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] + ' ')
    print('--- | --- | ---')
    print(' ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] + ' ')
    
# Player choose a marker either 'X' or 'O'
def player_marker():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input("Please select your marker 'X' or 'O': ").upper()
        
        if marker not in ('X', 'O'):
            print("Incorrect input, pick 'X' or 'O'!")
            
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Place the player's marker at choosen position
def place_marker(board, marker, position):
    pass

# Check to see of the picked position is free, if free return TRUE, if taken return FALSE
def space_check(board, position):
    pass

# Player choose the position where they want to place the marker, return the picked position
def player_choice(board):
    pass

# Check win if there are three of the same markers in a row
def win_check(board,marker):
    pass

# Check if the board is full, return TRUE if board is full, return FALSE if board is not full
def full_board_check(board):
    pass

# Choose who goes first with randomization
def choose_player():
    pass

# Asks if the player wants to play again
def replay():
    pass

