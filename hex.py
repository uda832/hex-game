# Exceptions
class InvalidMove(Exception):
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super(ValidationError, self).__init__(message)

        # Now for your custom code...
        self.errors = errors

#end-Exceptions


class HexNode:
    '''
        Represents a Hexagon game state -- i.e. board configuration
    '''

    # Constructor -- Takes a board 
    def __init__(self, board):
        self.board = board    # Note: a board is an adjacency list
        self._score = -999

    
    # # Override comparison op
    # def __eq__(self, otherHexNode):
        # return tuple(self.board) == tuple(otherHexNode.board)

    # Make HexNode hashable -- so it could used to check for existence in open/closed sets
    def __hash__(self):
        return hash(tuple(tuple(row) for row in board))

    # Make the node object printable
    def __str__(self):
        # IMPLEMENT_ME
        return out


    # score
    @property
    def score(self):
        # IMPLEMENT_ME
        pass

    @score.setter
    def score(self, s):
        _score = s

    
    def make_move(self, a, b, player):
        '''
            Adds an edge between vertices 'a' and 'b'
            Returns True if successful
        '''
        # Check if move is valid
        if a != b and self.board[a][b] == 0 and self.board[b][a] == 0:
            self.board[a][b] = self.board[b][a] = player
            return True
        else:
            raise InvalidMove("Cannot add an edge between nodes {} and {}".format(a,b))
    #end-make_move


    #end-h_score
        

    # Generates the states that correspond to the possbile moves
    def get_neighbors(self):
        '''
            Note: this function creates new HexNodes (Hex states) that
                  that result from each possible move
        '''
        # IMPLEMENT_ME
        # return [] # return the possible states
    #end-get_neighbors

#end-class HexNode


class HexGame:
    '''
        Implements the HexGame
    '''
    def __init__(self, starter):
        self.start = startHexNode
        self.start.g_score = 0
        self.goal = goalHexNode
        HexNode.GOAL_board = goalHexNode.board           # Set the static variable GOAL_board

    def play_game(self, starter, board=None):
        '''
            Starts the Hexagon game.

                Note: takes an optional parameter 'board' to start the game
        '''

        if board is None:


    #end-play_game


    def a_star(self):
        openList = []
        closedList = []
        parents = {}

        openList.append(self.start)             # Insert the start node into the Open list

        # Until openList becomes empty
        while openList:
            openList.sort(reverse=True, key=lambda x: x.f_score) # sort the openList to emulate a min-heap. Reverse the order so the .pop() can be used for convenience
            curHexNode = openList.pop()
            closedList.append(curHexNode)

            # Goal Found -- return the path
            if curHexNode == self.goal:
                return curHexNode.f_score
                # return buildPath(curHexNode)       # IMPLEMENT_ME

            # Iterate over neighbors of the current node
            for neighbor in curHexNode.get_neighbors():
                # Skip if already visited
                if neighbor in closedList:
                    continue

                if neighbor not in openList:
                    # Add to openList if discovered for the first time
                    openList.append(neighbor)
                else:
                    neighborIndex = openList.index(neighbor)

                    # If the current path cost is cheaper than the one found last time
                    if neighbor.g_score < openList[neighborIndex].g_score:
                        openList[neighborIndex].g_score = neighbor.g_score
                        parents[neighbor] = curHexNode

            #end-for
        #end-while

        print("Error: Failed to find solution")
        return -1
    #end-a_star


#end-class PuzzleSolvetempboard

def minimax(HexNode):
    ''' 
        Evaluates the minimax score for a given HexNode
    '''
    out = 0

    return out
        
def main():
    starter = int(input("Who should start the game? Enter player number: (1 for AI, 2 for Player)"))

    board = [[]]

    # Create the HexGame
    hex_game = HexGame(starter, board)
    hex_game.play_game()

#end-main




# Invoke driver
main()
