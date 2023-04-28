class Player:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id

        self.player_setps = []

    def add_player_step(self, step):
        self.player_setps.append(step)

    def __str__(self) -> str:
        return "This is Player"
