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
        return hash(tuple(tuple(row) for row in board))

    # Make the node object printable
    def __str__(self):
        out = ""

        for row in self.board:
            out += "".join(str(row)) + "\n"
        return out
    #end-__str__


    @property
    def minimax_score(self):
        return _score

    @minimax_score.setter
    def minimax_score(self, score):
        _score = score

    
    def make_move(self, a, b, player):
        '''
            Adds an edge between vertices 'a' and 'b'
            Returns True if successful
        '''
        # Check if move is valid
        try:
            if a != b and self.board[a][b] == 0 and self.board[b][a] == 0:
                self.board[a][b] = self.board[b][a] = player
            else:
                raise InvalidMove("Cannot add an edge between nodes {} and {}".format(a,b))
        except:
            raise InvalidMove("Cannot add an edge between nodes {} and {}".format(a,b))

    #end-make_move

    def check_for_triangle(self):
        '''
            Checks if the current node's board contains any solid or dashed triangles
            Returns:
                1 -- if a solid triangle exists.
                2 -- if a dashed triangle exists.
                0 -- otherwise
        '''
        result = 0



        return result
    #end-h_score
        
    # Generates the states that correspond to the possbile moves
    def get_neighbors(self, turn):
        '''
            Note: this function creates new HexNodes (Hex states) that
                  that result from each possible move for the current player
        '''
        out = []

        # Create a new HexNode for each possible move
        for i in range(6 - 1):
            if self.board[i]

            # IMPLEMENT_ME
        #end-for

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
                Stops the game once a triangle is found in the board

                Note: takes an optional parameter 'board' to start the game
        '''
        print("Starting game:\n")
        
        current_node = self.root

        # Continue playing until game is over
        while True:
            print(current_node)

            # Player's turn
            if self._turn == 1:
                current_node = self.handle_user_move(current_node, self._turn)
            # AI's turn
            else:
                neightbors = current_node.get_neighbors(self._turn)
                for node in neightbors:
                    node.minimax_score = minimax(node)

                current_node = max(neighbors, key=lambda elem: elem.minimax_score)

            # Check if the board has a triangle
            res = current_node.check_for_triangle() 

            # Keep playing
            if res == 0:
                self.change_turn()
                continue
            # Triangle exists -- Game over
            else:
                if res == 1:
                    print("Congratulations, you WIN !!!")
                elif res == 2:
                    print("Computer WINS.")
                print("Game Over")
                break
            #end-if-else
        #end-while True

        
        print(self.root)
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
                print("yaay. that works")
                break

        return node
    #end-handle_user_move

    def change_turn(self):
        self._turn = 2 if self._turn == 1 else 1



#end-class 

def minimax(node):
    '''
        Evaulates the current HexNode's score
    '''

    return score
#end-minimax

        
def main():
    starter = int(input("Who should start the game? Enter player number: (1 for AI, 2 for Player)"))

    board = [[0,0,0,0,0,0] for row in range(6)]

    # testNode = HexNode(board)
    # testNode.play_game()
    # print(testNode)

    # Create the HexGame
    hex_game = HexGame(starter, board)
    hex_game.play_game()

#end-main


def test():
    # starter = int(input("Who should start the game? Enter player number: (1 for AI, 2 for Player)"))
    print("--------Starting Test Driver method")
    board = [[0,0,0,0,0,0] for row in range(6)]

    testNode = HexNode(board)
    print(testNode)


    testNode.make_move(1,0,1)
    print(testNode)

    # # Create the HexGame
    # hex_game = HexGame(starter, board)
    # hex_game.play_game()

#end-main


# Invoke driver
main()
# test()
