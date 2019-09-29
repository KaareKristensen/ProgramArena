import uuid


class Player():

    def __init__(self, name: str, player_id: uuid, postion: (int, int)):
        self.__name = name
        self.__health = 10
        self.__move_count = 0
        self.__player_id = player_id
        self.__position = postion

    def get_position(self):
        return self.__position

    def get_name(self):
        return self.__name

    def get_player_id(self):
        return self.__player_id

    def move(self):
        raise NotImplementedError()

    def attack(self):
        raise NotImplementedError()

    def defend(self):
        raise NotImplementedError()

    def heal(self):
        raise NotImplementedError()

    def __repr__(self):
        return f"Player name: {self.__name}, health: {self.__health}"
