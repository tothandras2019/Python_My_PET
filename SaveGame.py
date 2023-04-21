import os
import json


class SaveGame:
    to_be_save = {}

    def save(game_state, game):
        SaveGame.to_be_save = game
        print(game)
        save_file = f'{game["players"][0]}-{game["players"][1]}_game_state.json'
        savefolder = "save"
        current_dir = os.getcwd()

        if not os.path.exists(os.path.join(current_dir, savefolder)):
            os.mkdir(savefolder)
            print(f"{savefolder} has been created!")

        jsonFile = json.dumps(game)
        with open(os.path.join(current_dir, savefolder, save_file), "wt") as file:
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
                return data

        except FileNotFoundError as err:
            print("NO FOLDER:", err)
