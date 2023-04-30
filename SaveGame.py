import os
import json
from player import Player


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

    # TODO: dead code:
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

    def load_with_players() -> list:
        curr_directory = os.getcwd()

        path_save = os.path.join(curr_directory, "save")
        files = os.listdir(path_save)

        saved_files_json = [file for file in files if file.endswith("json")]

        index = 0
        for of in saved_files_json:
            print(f"{index+1}) {of}")
            index += 1

        load_file = ""
        choose_file_input = input("Which game you need?")

        if int(choose_file_input):
            load_file = saved_files_json[int(choose_file_input) - 1]
            print(load_file)

        game_players = {}
        try:
            with open(os.path.join(path_save, load_file), "r", encoding="utf-8") as open_file:
                data = json.loads(open_file.read())
                data_keys = [key for key in data["players"].keys()]
                game_players[0] = Player(data["players"]["0"], int(data_keys[0]))
                game_players[1] = Player(data["players"]["1"], int(data_keys[1]))
                board = data["board"]

                return (game_players, board)
        except Exception as e:
            print("Exception occures", e)

    def choose_to_read(file_list: list) -> str:
        pass


# if __name__ == "__main__":
#     GameManager.load_with_players()
