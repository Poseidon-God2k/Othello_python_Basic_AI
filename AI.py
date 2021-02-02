from Othello import *
import sys

class AI_Othello(object):
    """AI player for Othello game engine"""

    def __init__(self, game, AI_player):
        self.game = game
        self.AI_player = AI_player

    def get_next_move(self):
        raise NotImplementedError("Inheritator forgot to implement this")

class Random_AI(AI_Othello):
    def __init__(self, game, AI_player):
        super(Random_AI, self).__init__(game, AI_player)

    def get_next_move(self):
        game_board = Othello.pre_built(self.game.board, self.AI_player)
        game_moves = game_board.get_possible_moves()
        # return tupple (col,row)
        return game_moves[0]

class Minmax_AI(AI_Othello):
    """Minmax using heuristic"""

    def __init__(self, game, AI_player, max_depth = 5):
        super(Minmax_AI, self).__init__(game, AI_player)
        self.max_depth = max_depth

    def get_next_move(self):
        return self.min_max(self.game.board,0, -sys.maxsize-1 , sys.maxsize, self.AI_player)

    def min_max(self, board, depth, alpja, beta, player):
        
