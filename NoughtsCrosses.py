#Noughts and Crosses

"""
-------
|X|X|O|
-------
|X|X|X|
-------
|X|X|X|
-------

-----------
|X|X|X|X|X|
-----------

checkwin:

Find a taken tile
look in a direction
if taken by same player, carry on
count the number in a row
if the count is same as board size
then they have won

TODO
when you choose to move to a tile with double digits, it only recognises the first digit
if you say C12, it will place it on C1

index out of bounds if they input tile not on board, e.g.

"""


class Board():
    def __init__(self, size):
        self.board = [[" " for i in range(size)] for j in range(size)]
        self.size = size
        self.top_len = 2*size+1
        
    def draw(self):
        rows = [chr(i) for i in range(65, 91)]
        print("   ", end="")
        for i in range(1, self.size+1): print(i, end=" ")
        print()
        for row_num, row in enumerate(self.board):
            print(" ","-"*self.top_len)
            print("", rows[int(row_num)], end="")
            for tile_num, tile in enumerate(row):
                print("|" + tile, end="")
                if tile_num == self.size-1:
                    print("|")
        print(" ", "-"*self.top_len)
        
    def place(self, x_pos, y_pos, piece):
        x_pos = ord(x_pos)-65

        if self.board[x_pos][y_pos-1] == " ":
            self.board[x_pos][y_pos-1] = piece
            return 0
        else:
            return 1

    def checkWin(self):
        #checks if win
        #check rows
        for row in self.board:
            temp = row[0]
            if temp != " ":
                for tile in row:
                    if temp == tile:
                        temp = tile

        temp = ""
        #check columns
        for i in range(self.size):
            if self.board[i][0] != " ":
                for row in self.board:
                    if tile != temp:
                        break
                    else:
                        if i > self.board.size:
                            return tile
            

        return False

    def checkFull(self):
        for row in self.board:
            for tile in row:
                if tile == " ":
                    return False
        return True
                    
        


def menu():
    run = True
    while run:
        if int(input("1 or 2 player")) == 1:
            singleplayer(int(input("What length of board???")))
        else:
            multiplayer(int(input("what length of board??")))
            

def singleplayer(board_size):
    run = True
    while run:
        pass

def multiplayer(board_size):
    run = True
    brd = Board(board_size)
    turn = 0
    turns = ["X", "O"]
    while not brd.checkFull() and not brd.checkWin():
        brd.draw()
        turn = 0**turn #if turn is 0, turn becomes 1, if turn is 1, turn becomes 0
        move = input("enter coord. e.g. A1 or B3\nenter / to exit")
        if move == "/":
            menu()
            return 1
        move = [move[0], move[1]]
        while brd.place(move[0], int(move[1]), turns[turn]):
            move = input("enter a coord that isnt taken please >:(")
    brd.draw()
    print("Game Over!")
    print(brd.checkWin())
    print("Do you want another game? (y/n)")
    if input().strip().lower() == "y":
        menu()
    
menu()
