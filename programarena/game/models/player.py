class Player():

    def __init__(self, name: str, position: (int, int)):
        self.name = name
        self.position = position
        self.health = 10

    def move(self):
        raise NotImplementedError()

    def attack(self):
        raise NotImplementedError()

    def defend(self):
        raise NotImplementedError()

    def heal(self):
        raise NotImplementedError()

    def __repr__(self):
        return f"Player name: {self.name}, health: {self.health}"
