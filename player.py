class Player:
    def __init__(self, name, color, value=1):
        self.name = name
        self.color = color
        self.value = value
        self.turn = False

    def __str__(self):
        return self.name

    def set_player_name(self, name):
        self.name = name
