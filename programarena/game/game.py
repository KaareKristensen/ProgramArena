from random import randint

from .models.player import Player


class Game:

    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width
        self.__board, self.__players = self.__setup_board(height, width)

    def __setup_board(self, height, width):
        board = [[0] * height for i in range(width)]
        players = [[0] * height for i in range(width)]
        return board, players

    def spawn_player(self, player_name: str):
        postion = (randint(0, self.__height),
                   randint(0, self.__width))
        while not self.__is_valid_postion(postion):
            postion = (randint(0, self.__height),
                       randint(0, self.__width))
        self.__players[postion[0], postion[1]] = 1
        raise NotImplementedError()

    def __is_valid_postion(self, postion: (int, int)):
        if self.__players[postion[0], postion[1]] == 0:
            return True
        return False

    def move(self, player: Player, direction: str):
        raise NotImplementedError()

    def do_action(self, player: Player):
        raise NotImplementedError()

    def end_turn(self):
        raise NotImplementedError()
