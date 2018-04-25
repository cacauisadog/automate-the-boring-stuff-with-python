import sys

board = {'top-L': 'a', 'top-M': 'b', 'top-R': 'c',
         'mid-L': 'd', 'mid-M': 'e', 'mid-R': 'f',
         'bot-L': 'g', 'bot-M': 'h', 'bot-R': 'i' }

def print_board(board):
    print()
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])

def play(turn):
    print('\nTurn for %s to play. Move on which space?' % turn)
    move = input()
    board[move] = turn

def check_win_condition():
    if (board['top-L'] == board['top-M'] and board['top-M'] == board['top-R']) or \
       (board['mid-L'] == board['mid-M'] and board['mid-M'] == board['mid-R']) or \
       (board['bot-L'] == board['bot-M'] and board['bot-M'] == board['bot-R']) or \
       (board['top-L'] == board['mid-L'] and board['mid-L'] == board['bot-L']) or \
       (board['top-M'] == board['mid-M'] and board['mid-M'] == board['bot-M']) or \
       (board['top-R'] == board['mid-R'] and board['mid-R'] == board['bot-R']) or \
       (board['top-L'] == board['mid-M'] and board['mid-M'] == board['bot-R']) or \
       (board['top-R'] == board['mid-M'] and board['mid-M'] == board['bot-L']):
        print('\nPlayer %s has won!' % turn)
        return True

print_board(board)
turn = 'O'

print('\nPlayer %s begins the game!' % turn)

for i in range(9):
    play(turn)
    print_board(board)
    if check_win_condition():
        sys.exit()

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print("\nNo one won!")
    

