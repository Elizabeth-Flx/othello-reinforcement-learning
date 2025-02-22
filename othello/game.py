






class OthelloBoard:
    def __init__(self):
        self.black = 0b000000000000000000000000000100000010000000000000000000000000000
        self.white = 0b000000000000000000000000001000000001000000000000000000000000000

        self.RIGHT_EDGE = 0b1000000010000000100000001000000010000000100000001000000010000000
        self.LEFT_EDGE = 0b0000000100000001000000010000000100000001000000010000000100000001

        self.current_player = 'B'


    def print_board(self):
        print("  0 1 2 3 4 5 6 7", end=" ")
        
        for i in range(64):

            if i % 8 == 0:
                print()
                print(i//8, end=" ")

            if (self.black >> i) & 1:
                print("B", end=" ") 
            elif (self.white >> i) & 1:
                print("W", end=" ")
            else:
                print("-", end=" ")
        print()
            
    def is_valid_move(self, move):
        # Check if move is within bounds
        if move < 0 or move > 63:
            print("out of bounds")
            return False

        # Check if square is occupied
        if ((self.black | self.white) >> move) & 1:
            print("occupied")
            return False
        
        opponent = self.black if self.current_player == 'W' else self.white
        player = self.black if self.current_player == 'B' else self.white

        directions = [-1, 1, -8, 8, -7, 7, -9, 9]

        flipped_positions = 0 # Store flipped positions

        for d in directions:

            flipped = 0 # Tmp flipped pieces storage
            i = move + d

            while (opponent >> i) & 1:

                # Check if move is out of bounds
                if (i < 0 or i > 63):
                    # print("out of bounds") 
                    break
                
                # Check for wrap across right edge
                if (d in [-7, 1, 9] and self.LEFT_EDGE >> i & 1):
                    # print("Right wrap detected")
                    break
                
                # Check for wrap across left edge
                if (d in [-9, -1, 7] and self.RIGHT_EDGE >> i & 1):
                    # print("Left wrap detected")
                    break
                
                flipped |= (1 << i) # set bit at position i
                i = i + d

            if (player >> i & 1 and flipped):
                flipped_positions |= flipped

        return flipped_positions
    
    def make_move(self, move):
        flips = self.is_valid_move(move)

        if (flips == 0):
            return False
        else:
            if (self.current_player == 'B'):
                self.black |= flips | (1 << move)
                self.white &= ~flips
            else:
                self.white |= flips | (1 << move)
                self.black &= ~flips

            self.current_player = 'W' if self.current_player == 'B' else 'B'
            return True


    def set_black(self, black):
        self.black = black

    def set_white(self, white):
        self.white = white
        

            
board = OthelloBoard()
# board.print_board()

board.set_black(288230378299195400)
board.set_white(704788029247488)

board.print_board()

print(board.is_valid_move(39))