import os
import json


class SaveGame:
    def save(game_state):
        savefolder = "save"
        current_dir = os.getcwd()

        if not os.path.exists(os.path.join(current_dir, savefolder)):
            os.mkdir(savefolder)
            print(f"{savefolder} has been created!")

        jsonFile = json.dumps(game_state)
        with open(os.path.join(current_dir, savefolder, "game_state.json"), "wt") as file:
            file.write(jsonFile)

    def load():
        file = "game_state.json"
        folder = "save"

        current_dir = os.getcwd()
        try:
            if not os.path.exists(os.path.join(current_dir, folder)):
                raise FileNotFoundError

            with open(os.path.join(current_dir, folder, file), "rt") as file:
                data = json.loads(file.read())
                print("DATA", data)

        except FileNotFoundError as err:
            print("NO FOLDER:", err)
