from games import *

class Mancala(Game):

    def __init__(self, board=[3,1]):
        moves = [(x, y) for x in range(len(board)) for y in range(1, board[x] + 1)]
        self.initial = GameState(to_move = 'MAX', utility = 0, board = board, moves = moves)

    def actions(self, state):
        return state.moves

    def result(self, state, move):
        board = state.board.copy()
        board[move[0]] -= move[1]
        moves = [(x, y) for x, y in state.moves if y <= board[x]]

        if len(moves) == 0:
            utility = 1
        else:
            utility = 0

        return GameState(to_move = 'MIN' if state.to_move == 'MAX' else 'MAX',
                         utility = utility, board = board, moves = moves)
    
    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        return state.utility if player == 'MIN' else -state.utility

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        return state.utility != 0 or len(state.moves) == 0

    def display(self, state):
        print("Board: ", state.board)

if __name__ == "__main__":
    man = Mancala() # Creating the game instance
    utility = man.play_game(alpha_beta_player, query_player) # computer moves first 
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
