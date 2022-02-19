class TicTacToe():
    def __init__(self):
        self.available = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.turn = 0
        self.token = ('0', 'X')
        self.token_turn = '0'

    def get_board(self):
        row1, row2, row3 = ' '.join(self.board[0:3]), ' '.join(self.board[3:6]), ' '.join(self.board[6:10])
        return ''.join([row1, '\n', row2, '\n', row3])

    def check_board_state(self, board):
        if len(set(board)) == 2:
            return 0
        # horizontal
        if len({board[0], board[1], board[2]}) == 1:
            if board[0] == 'X':
                return 1
            else:
                return -1
        if len({board[3], board[4], board[5]}) == 1:
            if board[3] == 'X':
                return 1
            else:
                return -1
        if len({board[6], board[7], board[8]}) == 1:
            if board[7] == 'X':
                return 1
            else:
                return -1
        # vertical
        if len({board[0], board[3], board[6]}) == 1:
            if board[0] == 'X':
                return 1
            else:
                return -1
        if len({board[1], board[4], board[7]}) == 1:
            if board[1] == 'X':
                return 1
            else:
                return -1
        if len({board[2], board[5], board[8]}) == 1:
            if board[2] == 'X':
                return 1
            else:
                return -1
        # diagonal
        if len({board[0], board[4], board[8]}) == 1:
            if board[4] == 'X':
                return 1
            else:
                return -1
        if len({board[6], board[4], board[2]}) == 1:
            if board[4] == 'X':
                return 1
            else:
                return -1
        return None

    # def update_board(self, where):
    #     if where in self.available:
    #         self.board[self.board.index(where)] = self.token_turn
    #         self.available.pop(self.available.index(where))

    # def update_copy_board(self, where, b, a):
    #     if where in a:
    #         b[b.index(where)] = 'X'
    #     a.pop(a.index(where))

    def new_turn(self):
        self.turn += 1
        self.token_turn = self.token[self.turn % 2]

    def best_move(self, board, token):
        print(board, token)
        token_max = self.token[1]
        token_min = self.token[0]
        # copy_board = self.board.copy()
        # copy_available = self.available.copy()
        # for i in copy_available:
        #     self.update_copy_board(i, copy_board, copy_available)

        # evaluate finish condition
        board_state = self.check_board_state(board)
        if board_state is not None:
            return (board_state, None)  # (board value, position)

        # generate possible movements
        available_moves = [c for c in board if c not in self.token]  # list comprehension
        minimax_move = None  # best move found
        sub_token = self.token[0] if token == self.token[1] else self.token[1]  # ternary operator -- alternate token
        for move in available_moves:
            sub_board = board.copy()
            sub_board[int(move) - 1] = token  # place token

            # evaluate movements
            sub_best_move = self.best_move(sub_board, sub_token)
            if minimax_move is None:
                minimax_move = (sub_best_move[0], move)
            elif token == token_max:
                if sub_best_move[0] > minimax_move[0]:
                    minimax_move = (sub_best_move[0], move)
            elif token == token_min:
                if sub_best_move[0] < minimax_move[0]:
                    minimax_move = (sub_best_move[0], move)
        return minimax_move



game = TicTacToe()
while True:
    if game.check_board_state(game.board) == 1:
        print('Congratulations X wins')
        print(game.get_board())
        break
    elif game.check_board_state(game.board) == -1:
        print('Congratulations 0 wins')
        print(game.get_board())
        break
    elif game.check_board_state(game.board) == 0:
        print('That was a draw')
        print(game.get_board())
        break
    else:
        print(game.get_board())
        print('It is the turn of', game.token_turn)
        if game.token_turn == 'X':
            box_to_replace = game.best_move(game.board, game.token_turn)[1]
        else:
            box_to_replace = input('Where do you want to move: ')
        game.board[int(box_to_replace) -1] = game.token_turn
        game.new_turn()
