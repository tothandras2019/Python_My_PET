from s_client.client import Client


class Player:
    def __init__(self, name="", id=0) -> None:
        self.name = name
        self.id = id

        self.player_setps: list = []

        self.set_player()

    def set_player(self) -> None:
        input_player_name = input("Kérem a nevét >> ")
        self.name = input_player_name

        Client(self)

    def add_player_step(self):
        user_input = input("Your turn:")
        user_input = user_input.upper()
        validated = self._validate_player_step(user_input)

        if not validated:
            print("Not valid step!")
            self.add_player_step()
            return

        self.player_setps.append(user_input)

    def _validate_player_step(self, step):
        row_alpha_helper = ["A", "B", "C"]
        if step[0] not in row_alpha_helper:
            print("-----wrong row!-----".upper())
            return False

        if int(step[1]) not in range(1, 4):
            print("-----wrong column!-----".upper())
            return False

        return True

    def __str__(self) -> str:
        return "This is Player"


Player()
