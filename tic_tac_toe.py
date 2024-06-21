class TicTacToe:

    def __init__(self):
        self.board = [' '] * 9
        self.turn = 'X'


    def get_winner(self):
        board = self.board

        # row
        for i in range(3):
            if board[i*3] != ' ' and board[i*3] == board[i*3 + 1] and board[i*3 + 1] == board[i*3 + 2]:
                return board[i*3]

        # col
        for i in range(3):
            if board[i] != ' ' and board[i] == board[i + 3] and board[i + 3] == board[i + 6]:
                return board[i]

        # main diagonal
        if board[0] != ' ' and board[0] == board[4] and board[4] == board[8]:
            return board[0]

        # sub diagonal
        if board[2] != ' ' and board[2] == board[4] and board[4] == board[6]:
            return board[2]

        return None


    def value(self):
        winner = self.get_winner()
        if winner == 'X':
            return self.board.count(' ')
        if winner == 'O':
            return -self.board.count(' ')
        return 0


    def children(self):
        if self.get_winner() is not None:
            return []

        children_lst = []
        for i, cell in enumerate(self.board):
            if cell == ' ':
                child = TicTacToe()
                child.board = [*self.board]
                child.board[i] = self.turn
                child.turn = 'X' if self.turn == 'O' else 'O'
                children_lst.append(child)
        return children_lst


    def __str__(self):
        line = f" {'-' * 11}\n"
        result = line
        for i in range(3):
            result += f'| {self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]} |\n'
            result += line
        return result
