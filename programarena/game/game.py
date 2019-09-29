from random import randint
import uuid

from .models.player import Player


class Game:

    def __init__(self, game_id: uuid, height: int, width: int):
        self.__game_id = game_id
        self.__board = self.__setup_board(height, width)
        self.__players = {uuid, Player}

    def __setup_board(self, height, width):
        board = [[0] * height for i in range(width)]
        return board

    def get_board(self):
        return self.__board

    def get_players(self):
        return self.__players

    def create_player(self, player_name: str):
        if not self.__is_valid_player_name(player_name):
            return None

        postion = (randint(0, self.__height),
                   randint(0, self.__width))
        while not self.__is_valid_postion(postion):
            postion = (randint(0, self.__height),
                       randint(0, self.__width))

        new_player_id = uuid.uuid4()
        new_player = Player(player_name, str(new_player_id), postion)
        self.__players[postion] = new_player
        return True

    def __is_valid_player_name(self, player_name: str):
        all_players = self.__players.values()
        for player in all_players:
            if player_name == player.get_name():
                return False
        return True

    def __is_valid_postion(self, postion: (int, int)):
        all_players = self.__players.values()
        for player in all_players:
            if player.get_position() == postion:
                return False
        return True

    def move(self, player: Player, direction: str):
        raise NotImplementedError()

    def do_action(self, player: Player):
        raise NotImplementedError()

    def end_turn(self):
        raise NotImplementedError()
