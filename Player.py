class Player():
    id = 0
    def __init__(self, name) -> None:
        self.name = name
        self.id = Player.id+1
        self.player_setps=[]
        pass

    def add_player_step(self, step):
        self.player_steps = step
        pass