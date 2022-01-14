"""Abstract class of player. 
Your players classes must inherit from this.
"""
import utils
import numpy as np


class AbstractPlayer:
    """Your player must inherit from this class.
    Your player class name must be 'Player', as in the given examples (SimplePlayer, LivePlayer).
    Use like this:
    from players.AbstractPlayer import AbstractPlayer
    class Player(AbstractPlayer):
    """

    def __init__(self, game_time):
        """
        Player initialization.
        """
        self.game_time = game_time
        self.board = np.array(24)
        self.directions = utils.get_directions

    def set_game_params(self, board):
        """Set the game parameters needed for this player.
        This function is called before the game starts.
        (See GameWrapper.py for more info where it is called)
        input:
            - board: np.array of the board.
        No output is expected.
        """
        raise NotImplementedError

    def make_move(self, time_limit):
        """Make move with this Player.
        input:
            - time_limit: float, time limit for a single turn.
        output:
            - direction: tuple, specifing the Player's movement, (pos, soldier, dead_opponent_pos)
        """
        raise NotImplementedError

    def set_rival_move(self, move):
        """Update your info, given the new position of the rival.
        input:
            - pos: tuple, the new position of the rival.
        No output is expected
        """
        raise NotImplementedError

    def is_player(self, player, pos1, pos2, board=None):
        """
        Function to check if 2 positions have the player on them
        :param player: 1/2
        :param pos1: position
        :param pos2: position
        :return: boolean value
        """
        if board is None:
            board = self.board
        if board[pos1] == player and board[pos2] == player:
            return True
        else:
            return False

    def check_next_mill(self, position, player, board=None):
        """
        Function to check if a player can make a mill in the next move.
        :param position: curren position
        :param board: np.array
        :param player: 1/2
        :return:
        """
        if board is None:
            board = self.board
        mill = [
            (self.is_player(player, 1, 2, board) or self.is_player(player, 3, 5, board)),
            (self.is_player(player, 0, 2, board) or self.is_player(player, 9, 17, board)),
            (self.is_player(player, 0, 1, board) or self.is_player(player, 4, 7, board)),
            (self.is_player(player, 0, 5, board) or self.is_player(player, 11, 19, board)),
            (self.is_player(player, 2, 7, board) or self.is_player(player, 12, 20, board)),
            (self.is_player(player, 0, 3, board) or self.is_player(player, 6, 7, board)),
            (self.is_player(player, 5, 7, board) or self.is_player(player, 14, 22, board)),
            (self.is_player(player, 2, 4, board) or self.is_player(player, 5, 6, board)),
            (self.is_player(player, 9, 10, board) or self.is_player(player, 11, 13, board)),
            (self.is_player(player, 8, 10, board) or self.is_player(player, 1, 17, board)),
            (self.is_player(player, 8, 9, board) or self.is_player(player, 12, 15, board)),
            (self.is_player(player, 3, 19, board) or self.is_player(player, 8, 13, board)),
            (self.is_player(player, 20, 4, board) or self.is_player(player, 10, 15, board)),
            (self.is_player(player, 8, 11, board) or self.is_player(player, 14, 15, board)),
            (self.is_player(player, 13, 15, board) or self.is_player(player, 6, 22, board)),
            (self.is_player(player, 13, 14, board) or self.is_player(player, 10, 12, board)),
            (self.is_player(player, 17, 18, board) or self.is_player(player, 19, 21, board)),
            (self.is_player(player, 1, 9, board) or self.is_player(player, 16, 18, board)),
            (self.is_player(player, 16, 17, board) or self.is_player(player, 20, 23, board)),
            (self.is_player(player, 16, 21, board) or self.is_player(player, 3, 11, board)),
            (self.is_player(player, 12, 4, board) or self.is_player(player, 18, 23, board)),
            (self.is_player(player, 16, 19, board) or self.is_player(player, 22, 23, board)),
            (self.is_player(player, 6, 14, board) or self.is_player(player, 21, 23, board)),
            (self.is_player(player, 18, 20, board) or self.is_player(player, 21, 22, board))
        ]

        return mill[position]

    def is_mill(self, position, board=None):
        if board is None:
            board = self.board
        """
        Return True if a player has a mill on the given position
        :param position: 0-23
        :return:
        """
        if position < 0 or position > 23:
            return False
        p = int(board[position])

        # The player on that position
        if p != 0:
            # If there is some player on that position
            return self.check_next_mill(position, p, board)
        else:
            return False

    def calculate_morris(self, board, player):
        """calculate the number of morris to the player in the current board"""
        mill_number = 0
        for index, x in enumerate(board):
            if x == player:
                if self.is_mill(index):
                    mill_number += 1 / 3

        return mill_number

    def number_of_morris(self, board):
        """this function calculates the diffirance in mill for both players """
        # TODO calculate the player morris

        return self.calculate_morris(self, board, 1) - self.calculate_morris(self, board, 2)


    def winningConfFunction(self, player, board=None):
        if board is None:
            board = self.board

        so_number = 0
        for i in board:
            if i == player:
                so_number += 1

        if so_number <= 2:
            return True
        # TODO check if blocks


    def number_of_pieces(self, player, board=None):
        if board is None:
            board = self.board
        so_number = 0
        for i in board:
            if i == player:
                so_number += 1

        return so_number

    def doubleMorriesFunctionAux(self,board,player,position):
        if board is None:
            board = self.board
        mill = [
            (self.is_player(player, 1, 2, board) and self.is_player(player, 3, 5, board)),
            (self.is_player(player, 0, 2, board) and self.is_player(player, 9, 17, board)),
            (self.is_player(player, 0, 1, board) and self.is_player(player, 4, 7, board)),
            (self.is_player(player, 0, 5, board) and self.is_player(player, 11, 19, board)),
            (self.is_player(player, 2, 7, board) and self.is_player(player, 12, 20, board)),
            (self.is_player(player, 0, 3, board) and self.is_player(player, 6, 7, board)),
            (self.is_player(player, 5, 7, board) and self.is_player(player, 14, 22, board)),
            (self.is_player(player, 2, 4, board) and self.is_player(player, 5, 6, board)),
            (self.is_player(player, 9, 10, board) and self.is_player(player, 11, 13, board)),
            (self.is_player(player, 8, 10, board) and self.is_player(player, 1, 17, board)),
            (self.is_player(player, 8, 9, board) and self.is_player(player, 12, 15, board)),
            (self.is_player(player, 3, 19, board) and self.is_player(player, 8, 13, board)),
            (self.is_player(player, 20, 4, board) and self.is_player(player, 10, 15, board)),
            (self.is_player(player, 8, 11, board) and self.is_player(player, 14, 15, board)),
            (self.is_player(player, 13, 15, board) and self.is_player(player, 6, 22, board)),
            (self.is_player(player, 13, 14, board) and self.is_player(player, 10, 12, board)),
            (self.is_player(player, 17, 18, board) and self.is_player(player, 19, 21, board)),
            (self.is_player(player, 1, 9, board) and self.is_player(player, 16, 18, board)),
            (self.is_player(player, 16, 17, board) and self.is_player(player, 20, 23, board)),
            (self.is_player(player, 16, 21, board) and self.is_player(player, 3, 11, board)),
            (self.is_player(player, 12, 4, board) and self.is_player(player, 18, 23, board)),
            (self.is_player(player, 16, 19, board) and self.is_player(player, 22, 23, board)),
            (self.is_player(player, 6, 14, board) and self.is_player(player, 21, 23, board)),
            (self.is_player(player, 18, 20, board) and self.is_player(player, 21, 22, board))
        ]

        return mill[position]

    def doubleMorriesFunction(self, board, player):
        double_number = 0
        for index, x in enumerate(board):
            if x == player:
                if self.doubleMorriesFunctionAux(board,player,index):
                    double_number += 1  #TODO Check if needed to change
        return double_number
    #TODO check what player we need to put in or both players .

    def isGoal(self, board):
        if self.winningConfFunction(self , 1, board):
            return True

    def succ(self , board):
        pass


    def closed_morris(self, board, player, curr_player_pos, moved_soldier):
        """ :param board - the current board
        :param curr_player_pos - 0-8 np array with soldiers positions
        :param moved_soldier - the idx of the soldier moved in the last round
        :return 1 if the player closed a mill with his last move,
        -1 if the rival closed a mill
        0 otherwise"""
        if board is None:
            board = self.board
        position = curr_player_pos[moved_soldier]
        "check if the moved soldier created a mill"
        if self.is_mill(position, board):
            if player == 1:
                return 1
            else:
                return -1
        return 0

    def get_number_of_blocked_pieces(self, board, soldier_pos):
        """ :param board - the current board
        :param soldier_pos - players positions on board
        :return the number of blocked soldiers """
        blocked_pieces = 0
        for index, position in np.ndenumerate(soldier_pos):
            if position > 0:
                directions = utils.get_directions(position)

                "if one direction is open, the soldier is not blocked"
                for direction in directions:
                    if board[direction] == 0:
                        break

                "no direction is open, soldier is blocked"
                blocked_pieces += 1
        return blocked_pieces

    def number_of_blocked_rival_pieces(self, board, soldier_pos, rival_soldiers_pos):
        """ :param board - the current board
        :param soldier_pos - players positions on board
        :param rival_soldiers_pos - rival players positions on board
        :return the difference between the number of rival's blocked pieces and
        my blocked pieces """
        my_blocked_pieces = self.get_number_of_blocked_pieces(board, soldier_pos)
        rival_blocked_pieces = self.get_number_of_blocked_pieces(board, rival_soldiers_pos)
        diff = my_blocked_pieces - rival_blocked_pieces
        return diff

    def get_number_of_2_pieces_per_player(self, board, player):
        """:param board - the current game board
        :param player - 1/2
        :return number of two piece configuration for a given player"""
        num_2_pieces = 0
        for position in range(0, 23):
            num_2_pieces += self.check_next_mill(position, player, board)
        return num_2_pieces

    def number_of_2_pieces_conf(self, board):
        """:param board - the current game board
        :return the difference between the number of my two piece configurations and
        my rival's two piece configurations"""
        my_2_pieces = self.get_number_of_2_pieces_per_player(board, 1)
        rival_2_pieces = self.get_number_of_2_pieces_per_player(board, 2)
        diff = my_2_pieces - rival_2_pieces
        return diff

    def phase1_heuristic(self, board, player, soldiers_pos, rival_soldiers_pos, moved_soldier):
        """:param board - the current game board
        :param soldiers_pos - players positions on board
        :param rival_soldiers_pos - rival players positions on board
        :param player - 1/2
        :return heuristics value for phase 1"""
        closed_mill = self.closed_morris(board, player, soldiers_pos, moved_soldier)
        value = closed_mill
        return value
        pass
