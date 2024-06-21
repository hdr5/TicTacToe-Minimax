from tic_tac_toe import TicTacToe
from minimax import minimax

def user(game):
    index = int(input('Enter index: '))
    while index < 0 or index >= 9 or game.board[index] != ' ':
        index = int(input('Incorrect index, Enter again: '))
    game.board[index] = game.turn
    game.turn = 'X' if game.turn == 'O' else 'O'
    return game


def computer(game):
    best_child = None
    if game.turn == 'X':
        max_value = float('-inf')
        for child in game.children():
            value = minimax(child, False)
            if value > max_value:
                max_value = value
                best_child = child
    else:
        min_value = float('inf')
        for child in game.children():
            value = minimax(child, True)
            if value < min_value:
                min_value = value
                best_child = child
    return best_child


# decorators (time, cache), main, colors, command line tools
if __name__  == '__main__':
    game = TicTacToe()
    print(game)
    is_computer = True
    while ' ' in game.board and game.get_winner() is None:
        if is_computer:
            game = computer(game)
        else:
            game = user(game)

        is_computer = not is_computer
        print(game)


    winner = game.get_winner()
    if winner is None:
        print('It is a draw')
    else:
        print(f'{winner} is the winner')
