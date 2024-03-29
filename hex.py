# Author: Oyun-Undrakh Yeruultsengel
# Hex Game -- Interactive game of Hexagon. AI implemented using Alpha-Beta pruning
# 03/25/2018

import copy
import random
from math import inf


# Exceptions
class InvalidMove(Exception):
    pass


#end-Exceptions


class HexNode:
    '''
        Represents a Hexagon game state -- i.e. board configuration

            Note: the 'board' is an adjacency matrix (i.e. 6x6 two-dimensional list of integers)
                Example: 
                board[0][1] = 1 indicates that a solid line exists between the dots 0 and 1
                board[0][1] = 2 indicates that a dashed line exists between the dots 0 and 1

    '''

    # Constructor -- Takes a board 
    def __init__(self, board):
        self.board = board    # Note: a board is an adjacency matrix
        self._score = None

    
    # # Override comparison op
    # def __eq__(self, otherHexNode):
        # return tuple(self.board) == tuple(otherHexNode.board)

    # Make HexNode hashable -- so it could used to check for existence in open/closed sets
    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.board))

    # Make the node object printable
    def __str__(self):
        out = ""

        for row in self.board:
            out += "".join(str(row)) + "\n"
        return out
    #end-__str__


    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    
    def make_move(self, a, b, player):
        '''
            Adds an edge between vertices 'a' and 'b'
            Returns True if successful
        '''
        # Check if move is valid
        try:
            if a != b and self.board[a][b] == 0:
                self.board[a][b] = player
            else:
                raise InvalidMove("Cannot add an edge between nodes {} and {}".format(a,b))
        except:
            raise InvalidMove("Cannot add an edge between nodes {} and {}".format(a,b))

    #end-make_move

    def check_for_triangle(self):
        '''
            Checks if the current node's board contains a solid or dashed triangle

            Return type: tuple(int, tuple(int,int,int)) 
                First element (int) indicates what type of triangle exists.
                    1 -- if a solid triangle exists.
                    2 -- if a dashed triangle exists.
                    0 -- if no triangle exists
                Second element (tuple(int,int,int)) indicates the location of the triangle
                    example: (1,2,3) means the triangle is formed between dots 1, 2, and 3
            Examples:
                (1, (1,2,3)) -- There exists a solid triangle between dots 1, 2, and 3
                (2, (2,4,5)) -- There exists a dashed triangle between dots 2, 4, and 5

        '''
        for i in range(0, 4):
            for j in range(i + 1, 5):
                for k in range(j + 1, 6):
                    if self.board[i][j] == self.board[j][k] == self.board[i][k] != 0:
                        # print("TEST: Triangle found: {} {} {}".format(i,j,k))
                        tri_type = self.board[i][j]
                        return (tri_type, (i, j, k))
                #end-for-k
            #end-for-j
        #end-for-i

        # No triangle found
        # print("TEST: no triangle found")
        return (0, None)
    #end-h_score
        
    # Generates the states that correspond to the possbile moves
    def get_neighbors(self, turn):
        '''
            Note: this function creates new HexNodes (Hex states) that
                  that result from each possible move for the specified player
        '''
        out = []

        # Create a new HexNode for each possible move and add to the 'out' list
        #----------------------------------------------
        for i in range(0, 6):
            for j in range(i + 1, 6):
                if self.board[i][j] != 0:               # Ensure that no line exists between the dots at index i and j
                    continue
                
                temp_board = copy.deepcopy(self.board)  # Create a deep copy of the board
                new_node = HexNode(temp_board)          # Construct a new HexNode 
                new_node.make_move(i, j, turn)          # Make the possible move
                out.append(new_node)                    # Add to the neighbors list

            #end-for-j
        #end-for-i
        
        return out
    #end-get_neighbors

#end-class HexNode


class HexGame:
    '''
        Implements the HexGame
    '''
    def __init__(self, starter, board=None):
        '''
            Note: the 'board' is an adjacency matrix (i.e. 6x6 two-dimensional list of integers)
                Example: 
                board[0][1] = 1 indicates that a solid line exists between the dots 0 and 1
                board[0][1] = 2 indicates that a dashed line exists between the dots 0 and 1
                board[0][1] = 0 indicates there's no line between the dots 0 and 1

        '''
        self._starter = starter
        self._turn = starter
        self._maximizer = starter
        self._minimizer = 2 if starter == 1 else 1

        # Set board to empty if it was not passed
        root_board = board if board else [[0,0,0,0,0,0] for row in range(6)]

        self.root = HexNode(root_board)
    #end-__init__


    def play_game(self):
        '''
            Starts the Hexagon game.
                Changes turns between the AI and the user
                Handles user's input/move and makes the AI's move by selecting the best move by using Alpha-Beta Pruning search.
                Stops the game once a triangle is found in the board

                Note: takes an optional parameter 'board' to start the game
        '''
        print("Starting game:\n")
        
        current_node = self.root
        
        # Handle start
        if self._starter == 1:
            # AI starts -- make an arbitrary opening move
            current_node = random.choice(current_node.get_neighbors(1))
            self._turn = 2
        else:
            # Player starts
            self._turn = 2



        # Continue playing until game is over
        while True:
            print(current_node)

            # Player's turn
            if self._turn == 2:
                print("Your turn.")
                current_node = self.handle_user_move(current_node, self._turn)
            # AI's turn
            else:
                print("AI's turn.\nThe AI is thinking to pick a move...")
                best_value = -inf
                best_move = current_node
                neighbors = current_node.get_neighbors(self._turn)

                for neighbor_node in neighbors:
                    neighbor_node.score = alpha_beta(neighbor_node, turn=self._turn, alpha=-inf, beta=inf, depth=0)

                    if neighbor_node.score > best_value:
                        best_value = neighbor_node.score
                        best_move = neighbor_node
                #end-for

                current_node = best_move
            #end-if-else

            # Check if the board has a triangle
            res,tri_loc = current_node.check_for_triangle() 

            # Keep playing
            if res == 0:
                self.change_turn()
                continue
            # Triangle exists -- Game over
            else:
                print(current_node)
                # 1 -- Solid triangle found
                if res == 1:
                    print("Congratulations, you WIN !!!")
                # 2 -- Dashed triangle found
                elif res == 2:
                    print("Computer WINS.")
                print("{} triangle found at {} {} {}".format("Solid" if res == 1 else "Dashed", tri_loc[0], tri_loc[1], tri_loc[2]))
                print("Game Over")
                break
            #end-if-else
        #end-while True
    #end-play_game

    def handle_user_move(self, node, turn):
        '''
            Prompts the user to enter a move.
            Keeps prompting until a valid move is entered.
            Once a valid move is entered, makes the move
        '''
        a = b = -1

        while True:
            try:
                user_input = input("Enter the name of the nodes to connect (example: 0 1): ")
                a = int(user_input.split(" ")[0])
                b = int(user_input.split(" ")[1])

                if a < 0 or a > 5 or b < 0 or b > 5:
                    raise ValueError

                node.make_move(a, b, turn)

            except (ValueError,IndexError,InvalidMove):
                print("Sorry, the entered input is not valid. Try again.")
                continue
            else:
                # print("yaay. that works")
                break

        return node
    #end-handle_user_move

    def change_turn(self):
        self._turn = 2 if self._turn == 1 else 1



#end-class 


def alpha_beta(node, turn=1, alpha=-inf, beta=inf, depth=0):
    '''
        Evaulates the current HexNode's score for the current player (which is specified by the turn parameter)
            turn=1 -- maximize
            turn=2 -- minimize

            Note: by default, calculates the score for turn=1 (i.e. max)
    '''
    
    # print("------------------------alpha_beta with depth={}".format(depth))
    # print(node)


    # Check if the current node has a triangle
    has_triangle, tri_loc = node.check_for_triangle()

    '''
        Return 1 if a solid triangle exists
        Return -1 if a dashed triangle exists
    '''
    if has_triangle:
        # print("TEST-TERMINAL-REACHED: current node")
        # print(tri_loc)
        # input("Press enter to continue")
        return -1 if has_triangle == 1 else 1

    # if depth > 15:
        # return 0

    # Max
    if turn == 1:
        best_val = -inf
        neighbors = node.get_neighbors(turn=2)
        for neighbor_node in neighbors:
            neighbor_node.score = alpha_beta(neighbor_node, turn=2, alpha=alpha, beta=beta, depth=depth + 1)

            best_val = max(best_val, neighbor_node.score)
            alpha = max(best_val, alpha)

            if beta <= alpha:
                # print("beta cutoff: {} {} at depth {}".format(alpha, beta,depth))
                break       # Perform Beta cut-off
        return best_val
    
    # Min
    elif turn == 2:
        best_val = inf
        neighbors = node.get_neighbors(turn=1)
        for neighbor_node in neighbors:
            neighbor_node.score = alpha_beta(neighbor_node, turn=1, alpha=alpha, beta=beta, depth=depth + 1)

            best_val = min(best_val, neighbor_node.score)
            beta = min(best_val, beta)

            if beta <= alpha:
                # print("alpha cutoff: {} {} at depth {}".format(alpha, beta,depth))
                break       # Perorm Alpha cut-off

        return best_val
    
    else:
        raise ValueError
#end-alpha_beta

        

# Driver method
def main():
    starter = int(input("Who should start the game?\nEnter player number (1 for AI, 2 for Player): "))

    # Initialize board to empty (i.e. no lines)
    board = [[0,0,0,0,0,0] for row in range(6)]

    # Create the HexGame
    hex_game = HexGame(starter, board)
    hex_game.play_game()

#end-main


def test():
    # starter = int(input("Who should start the game? Enter player number: (1 for AI, 2 for Player)"))
    print("--------Starting Test Driver method")

    board = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]
        ]

    # board = [
        # [0,0,0,2,1,0],
        # [0,0,1,1,2,0],
        # [0,0,0,2,0,2],
        # [0,0,0,0,1,0],
        # [0,0,0,0,0,0],
        # [0,0,0,0,0,0]
        # ]

    # board = [
        # [0, 0, 0, 0, 0, 2],
        # [0, 0, 1, 0, 0, 1],
        # [0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 2, 1],
        # [0, 0, 0, 0, 0, 2],
        # [0, 0, 0, 0, 0, 0]
        # ]


    # print("------------------Starting alpha_beta")
    # test_node = HexNode(board)
    # # test_node.check_for_triangle()
    # alpha_beta(test_node, 1, -inf, inf, 0)
    # print(test_node)




    # test_node.make_move(1,0,1)
    # print(test_node)

    # # Create the HexGame
    # hex_game = HexGame(starter, board)
    # hex_game.play_game()

#end-main


# Invoke driver
main()
# test()
