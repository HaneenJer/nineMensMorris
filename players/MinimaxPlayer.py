"""
MiniMax Player
"""
import numpy as np

from players.AbstractPlayer import AbstractPlayer


# TODO: you can import more modules, if needed

class Player(AbstractPlayer):
    def __init__(self, game_time):
        AbstractPlayer.__init__(self, game_time)  # keep the inheritance of the parent's (AbstractPlayer) __init__()
        # TODO: initialize more fields, if needed, and the AlphaBeta algorithm from SearchAlgos.py
        self.turn = 0
        self.my_pos = None
        self.rival_pos = None

    def set_game_params(self, board):
        """Set the game parameters needed for this player.
        This function is called before the game starts.
        (See GameWrapper.py for more info where it is called)
        input:
            - board: np.array, of the board.
        No output is expected.
        """
        # TODO: erase the following line and implement this function.
        self.my_pos = np.full(9, -1)
        self.rival_pos = np.full(9, -1)
        self.board = board
        raise NotImplementedError

    def make_move(self, time_limit):
        """Make move with this Player.
        input:
            - time_limit: float, time limit for a single turn.
        output:
            - direction: tuple, specifing the Player's movement
        """
        if self.turn < 18:
            move = self._stage_1_move()
            self.turn += 1
            return move
        # TODO: erase the following line and implement this function.
        raise NotImplementedError

    def set_rival_move(self, move):
        """Update your info, given the new position of the rival.
        input:
            - move: tuple, the new position of the rival.
        No output is expected
        """
        # TODO: erase the following line and implement this function.
        raise NotImplementedError

    ########## helper functions in class ##########
    # TODO: add here helper functions in class, if needed

    def _stage_1_choose_cell_and_soldier_to_move(self):
        # TODO: choose cell to move
        # TODO: choose soldier
        cell = None
        soldier_that_moved = None
        return cell, soldier_that_moved

    def _choose_rival_cell_to_kill(self):
        # TODO: choose cell heuristic
        rival_cell = None
        return rival_cell

    def _make_mill_get_rival_cell(self):
        rival_cell = self._choose_rival_cell_to_kill()
        rival_idx = np.where(self.rival_pos == rival_cell)[0][0]
        self.rival_pos[rival_idx] = -2
        self.board[rival_cell] = 0
        return rival_cell

    def _stage_1_move(self) -> tuple:
        cell, soldier_that_moved = self._stage_1_choose_cell_and_soldier_to_move()
        self.my_pos[soldier_that_moved] = cell
        self.board[cell] = 1

        rival_cell = -1 if not self.is_mill(cell) else self._make_mill_get_rival_cell()
        return cell, soldier_that_moved, rival_cell

    ########## helper functions for AlphaBeta algorithm ##########
    # TODO: add here the utility, succ, an
