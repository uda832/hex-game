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
        self._score = -999

    
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


    # score
    @property
    def score(self):
        return _score
        

    @score.setter
    def score(self, s):
        _score = s

    
    def make_move(self, a, b, player):
        '''
            Adds an edge between vertices 'a' and 'b'
            Returns True if successful
        '''
        # Check if move is valid
        try:
            if a != b and self.board[a][b] == 0 and self.board[b][a] == 0:
                self.board[a][b] = player
                self.board[b][a] = player
            else:
                raise InvalidMove("Cannot add an edge between nodes {} and {}".format(a,b))
        except:
            raise InvalidMove("Cannot add an edge between nodes {} and {}".format(a,b))

    #end-make_move


    #end-h_score
        

    # # Generates the states that correspond to the possbile moves
    # def get_neighbors(self):
        # '''
            # Note: this function creates new HexNodes (Hex states) that
                  # that result from each possible move
        # '''
        # # IMPLEMENT_ME
        # # return [] # return the possible states
    # #end-get_neighbors

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
        self._maximizer = starter
        self._minimizer = 2 if starter == 1 else 1

        # Set board to empty if it was not passed
        root_board = board if board else [[0,0,0,0,0,0] for row in range(6)]

        self.root = HexNode(root_board)


    def play_game(self):
        '''
            Starts the Hexagon game.

                Note: takes an optional parameter 'board' to start the game
        '''
        print("Starting game:\n")

        
        print(self.root)
    #end-play_game



#end-class 

def minimax(HexNode):
    ''' 
        Evaluates the minimax score for a given HexNode
    '''
    out = 0

    return out
#end-minimax
        
def main():
    starter = int(input("Who should start the game? Enter player number: (1 for AI, 2 for Player)"))

    board = [[0,0,0,0,0,0] for row in range(6)]

    testNode = HexNode(board)
    print(testNode)

    # # Create the HexGame
    # hex_game = HexGame(starter, board)
    # hex_game.play_game()

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


# Invoke test driver
test()
