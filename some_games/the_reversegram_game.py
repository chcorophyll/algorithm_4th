"""
references:https://inventwithpython.com/invent4thed/chapter15.html
"""

import random
import sys


WIDTH = 8
HEIGHT = 8


def draw_board(board):
    print('  12345678  ')
    print(' +--------+ ')
    for y in range(HEIGHT):
        print('{}|'.format(y+1), end='')
        for x in range(WIDTH):
            print(board[y][x], end='')
        print('|{}'.format(y + 1))
    print(' +--------+ ')
    print('  12345678  ')


def get_new_board():
    board = [[' '] * WIDTH for i in range(HEIGHT)]
    return board


def is_on_board(y, x):
    return 0 <= y < HEIGHT and 0 <= x < WIDTH


def get_board_with_valid_moves(board, tile):
    copied_board = get_board_copy(board)
    for y, x in get_valid_moves(copied_board, tile):
        copied_board[y][x] = '.'
    return copied_board


def is_valid_move(board, tile, start_y, start_x):
    if board[start_y][start_x] != ' ' or not is_on_board(start_y, start_x):
        return False
    other_tile = 'O' if tile == 'X' else 'X'
    to_flips = []
    directions = [[0, 1], [1, 1], [1, 0], [1, -1],
                  [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    for offset_y, offset_x in directions:
        y, x = start_y + offset_y, start_x + offset_x
        while is_on_board(y, x) and board[y][x] == other_tile:
            y += offset_y
            x += offset_x
            if is_on_board(y, x) and board[y][x] == tile:
                while True:
                    y -= offset_y
                    x -= offset_x
                    if y == start_y and x == start_x:
                        break
                    to_flips.append([y, x])
    if len(to_flips) == 0:
        return False
    return to_flips


def get_valid_moves(board, tile):
    valid_moves = []
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if is_valid_move(board, tile, y, x):
                valid_moves.append([y, x])
    return valid_moves


def get_board_score(board):
    x_score = 0
    o_score = 0
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if board[y][x] == "X":
                x_score += 1
            elif board[y][x] == "O":
                o_score += 1
    return {'X': x_score, 'O': o_score}


def enter_player_tile():
    tile = ''
    while not (tile != 'X' or tile != 'O'):
        print('Do you want to be X or O ?')
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def make_move(board, tile, start_y, start_x):
    flips = is_valid_move(board, tile, start_y, start_x)
    if not flips:
        return False
    board[start_y][start_x] = tile
    for y, x in flips:
        board[y][x] = tile
    return True


def get_board_copy(board):
    new_board = get_new_board()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            new_board[y][x] = board[y][x]
    return new_board


def is_on_corner(y, x):
    return (y == 0 or y == HEIGHT - 1) and (x == 0 or y == WIDTH - 1)


def get_player_move(board, tile):
    digits_y = [str(i+1) for i in range(HEIGHT)]
    digits_x = [str(i+1) for i in range(WIDTH)]
    while True:
        print('Enter your move, "quit" to end the game, or "hints" to toggle hints.')
        move = input().lower()
        if move == 'quit' or move == 'hints':
            return move
        if len(move) == 2 and move[0] in digits_y and move[1] in digits_x:
            y = int(move[0]) - 1
            x = int(move[1]) - 1
            if not is_valid_move(board, tile, y, x):
                continue
            else:
                break
        else:
            print('That is not a valid move. Enter the column (1-8) and then the row(1 - 8).')
            print('For example, 81 will move on the top-right corner.')
    return [y, x]


def get_computer_move(board, tile):
    possible_moves = get_valid_moves(board, tile)
    random.shuffle(possible_moves)
    for y, x in possible_moves:
        if is_on_corner(y, x):
            return [y, x]
    best_score = -1
    for y, x in possible_moves:
        copied_board = get_board_copy(board)
        make_move(copied_board, tile, y, x)
        score = get_board_score(copied_board)[tile]
        if best_score < score:
            best_move = [y, x]
            best_score = score
    return best_move


def print_score(board, player_tile, computer_tile):
    scores = get_board_score(board)
    print('You: %s points. Computer: %s points.' % (scores[player_tile], scores[computer_tile]))


def play_games(player_tile, computer_tile):
    show_hints = False
    turn = who_goes_first()
    board = get_new_board()
    board[3][3] = 'X'
    board[4][3] = 'O'
    board[3][4] = 'O'
    board[4][4] = 'X'
    while True:
        player_valid_moves = get_valid_moves(board, player_tile)
        computer_valid_moves = get_valid_moves(board, computer_tile)
        if len(player_valid_moves) == 0 and len(computer_valid_moves) == 0:
            return board
        elif turn == 'player':
            if player_valid_moves:
                if show_hints:
                    valid_move_board = get_board_with_valid_moves(board, player_tile)
                    draw_board(valid_move_board)
                else:
                    draw_board(board)
                print_score(board, player_tile, computer_tile)
                move = get_player_move(board, player_tile)
                if move == 'quit':
                    print('Thanks for playing!')
                    sys.exit()
                elif move == 'hints':
                    show_hints = not show_hints
                    continue
                else:
                    make_move(board, player_tile, *move)
            turn = 'computer'
        elif turn == 'computer':
            if computer_valid_moves:
                draw_board(board)
                print_score(board, player_tile, computer_tile)
                input('Press Enter to see the computer\'s move.')
                move = get_computer_move(board, computer_tile)
                make_move(board, computer_tile, *move)
            turn = 'player'


print('Welcome to Reversegam!')
player_tile, computer_tile = enter_player_tile()
while True:
    final_board = play_games(player_tile, computer_tile)
    draw_board(final_board)
    scores = get_board_score(final_board)
    print('X scored %s points. O scored %s points.' % (scores['X'], scores['O']))
    if scores[player_tile] > scores[computer_tile]:
        print('You beat the computer by %s points! Congratulations!' % (scores[player_tile] - scores[computer_tile]))
    elif scores[player_tile] < scores[computer_tile]:
        print('You lost. The computer beat you by %s points.' % (scores[computer_tile] - scores[player_tile]))
    else:
        print('The game was a tie!')
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break

