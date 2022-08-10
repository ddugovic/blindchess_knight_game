import random
from itertools import product
letter_to_digit = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
digit_to_letter = {u:v for v,u in letter_to_digit.items()}

def human_to_computer(human_co_ord):
    """ A small function to turn human co ordinates into the number tuple required """
    letter = letter_to_digit[human_co_ord[0].capitalize()]
    number = int(human_co_ord[1])
    return (letter,number)
def computer_to_human(computer_co_ord):
    """ A small function to turn computer co ordinates into the human readable string """
    letter = digit_to_letter[computer_co_ord[0]]
    number = computer_co_ord[1]
    return f"{letter}{number}"

def validate_move(move):
    """ a small function to make sure a move is valid """
    try:
        move_comp = human_to_computer(move)
        return move_comp[0]<=8 and move_comp[1]<=8
    except:
        return False

def make_pos():
    """ a function to make random co-ordinates for the knight and queen that are not the same """
    kx,ky,qx,qy = 0,0,0,0
    while (kx,ky) == (qx,qy):
        kx,ky,qx,qy = random.randint(1,8),random.randint(1,8),random.randint(1,8),random.randint(1,8)
    return (kx,ky),(qx,qy)







class Knight:
    def __init__(self,pos,queen_pos):
        self.pos = pos
        self.queen_pos = queen_pos

    def position(self):
        """ just returns knights current position """
        return self.pos

    def queen_sights(self):
        """ a method to generate a list of valid queen moves """
        valid_queen_moves = []
        queenpos = [self.queen_pos[0],self.queen_pos[1]]
        directions = [(1, 0), (0, 1), (1, 1), (1, -1),(-1, 0), (0, -1), (-1, -1), (-1, 1)]
        for dir_ in directions:
            for i in range(1,9):
                col = queenpos[0] + i*dir_[0]
                row = queenpos[1] + i*dir_[1]
                if row < 9 and row > 0 and col < 9 and col > 0:
                    if (col,row) not in valid_queen_moves:
                        valid_queen_moves.append((col,row))
        return valid_queen_moves

    def valid_moves(self):
        """ generates a list of valid moves for the knight """
        x, y = self.pos
        moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
        moves = [(x,y) for x,y in moves if x >= 1 and y >= 1 and x < 9 and y < 9]
        return moves

    def validate_move(self,move):
        """ validates a knights move, making sure it is legal and not in the eyesight of the queen """
        if move in self.valid_moves():
            if move not in self.queen_sights():
                return True
            else:
                print(f"that would come into the sight of the queen on {computer_to_human(self.queen_pos)}")

    def move_knight(self,move):
        """ updates knights position if a legal move """
        if self.validate_move(move):
            self.pos = move
            print(f"your knight has moved to {computer_to_human(self.pos)}")
        else:
            print(f"sorry, {computer_to_human(move)} is not a valid move")

    def check_win(self):
        """ a method to check if the game is over """
        return self.pos == self.queen_pos

    def dump_info(self):
        """ diagnostic info dump for dev """
        queen_move_list = list(map(computer_to_human,self.queen_sights()))
        knight_move_list = list(map(computer_to_human,self.valid_moves()))
        print(f"the queen is on {computer_to_human(self.queen_pos)} and it's valid moves are {queen_move_list} the knight is on {computer_to_human(self.pos)} and it's valid moves are {knight_move_list}")



""" game starts proper """

knights_position,queen_position = make_pos()
kn = Knight(knights_position,queen_position)

print(f"your position with the knight is {computer_to_human(kn.position())}")
print(f"the queen is on {computer_to_human(queen_position)}")
while not kn.check_win():
    move = input("please type in a move: \n")
    move_comp = human_to_computer(move)
    kn.move_knight(move_comp)
print("well done you got the queen!")
