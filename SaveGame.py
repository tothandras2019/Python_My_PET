import os
import json


class GameManager:
    to_be_save = {}

    def save(game_state, game):
        GameManager.to_be_save = game

        save_file = f'{game["players"][0]}-{game["players"][1]}_game_state.json'
        savefolder = "save"
        current_dir = os.getcwd()

        if not os.path.exists(os.path.join(current_dir, savefolder)):
            os.mkdir(savefolder)
            print(f"{savefolder} has been created!")

        jsonFile = json.dumps(game)
        with open(os.path.join(current_dir, savefolder, save_file), "wt", encoding="utf-8") as file:
            file.write(jsonFile)

    def load() -> list:
        file = "game_state.json"
        folder = "save"

        current_dir = os.getcwd()
        try:
            if not os.path.exists(os.path.join(current_dir, folder)):
                raise FileNotFoundError

            with open(os.path.join(current_dir, folder, file), "rt") as file:
                data = json.loads(file.read())
                GameManager.to_be_save = {}
                return data

        except FileNotFoundError as err:
            print(f"{file} file is not found:", err)

    def load_with_players(players: dict) -> dict:
        curr_directory = os.getcwd()

        path_save = os.path.join(curr_directory, "save")
        files = os.listdir(path_save)

        onlyfiles = [file for file in files if file.endswith("json")]
        index = 0

        for of in onlyfiles:
            print(f"{index+1}) {of}")
            index += 1

        load_file = ""
        choose_file_input = input("Which game you need?")

        if int(choose_file_input):
            load_file = onlyfiles[int(choose_file_input) - 1]
            print(load_file)
            pass

        # try:
        #     with open() as open_file:
        #         pass

        # except FileExistsError:
        #     pass

    def choose_to_read(file_list: list) -> str:
        pass


if __name__ == "__main__":
    GameManager.load_with_players({})
