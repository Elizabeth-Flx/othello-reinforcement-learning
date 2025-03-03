import numpy as np

class TTTBoard:
    def __init__(self):
        self.board = np.array([
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ])
        self.placed_pieces = 0
        self.current_player = 1

    def print_board(self):
        for i in range(3):
            print()
            print(i, end=' ')
            for j in range(3):
                if (self.board[i][j] == 1): 
                    print('B', end=' ')
                elif (self.board[i][j] == -1):
                    print('W', end=' ')

    def is_valid_move(self, i, j):
        return self.board[i][j]==0
    
    def make_move(self, i, j):
        if not self.is_valid_move(i, j):
            print("occupied")
            return False

        self.board[i][j] = self.current_player
        self.current_player = 1 if self.current_player == -1 else -1
        return True
    
    def get_valid_moves(self):
        valid_moves = []
        for i in range(3):
            for j in range(3):
                if self.is_valid_move(i,j):
                    valid_moves.append((i,j))
        return valid_moves

    # This is very inefficient
    def is_game_over(self):
        for i in range(3):
            row = self.board[i,:]
            col = self.board[:,i]

            if np.all(col == col[0]) and col[0] != 0:
                return col[0]
            if np.all(row == row[0]) and row[0] != 0:
                return row [0]
            
        diag1 = np.diag(self.board)
        diag2 = np.diag(np.flipr(self.board))

        if np.all(diag1 == diag1[0]) and diag1[0] != 0:
            return diag1[0]
        if np.all(diag2 == diag2[0]) and diag2[0] != 0:
            return diag2[0]

        return 0

