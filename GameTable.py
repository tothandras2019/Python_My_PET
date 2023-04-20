from Player import Player
from SaveGame import SaveGame
import copy


class Board:
    menu = ["#Type field (example: A3+enter)", "#Quit = Q", "#Save = S", "#Load game = L"]
    board_table = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    row_dict = {"A": 0, "B": 1, "C": 2}
    column_dict = {"1": 0, "2": 1, "3": 2}

    def __init__(self) -> None:
        self.isWinner_field = False
        self.players = {}

        self.init_players()

        self.actual_player_id = self.players[0].id
        print("ID", self.players[0].id)

        self.print_table_to_console(Board.board_table)
        self.table_states_collection = []

        self.next_round_player_steps(self.actual_player_id)

    def init_players(self):
        for index in range(0, 2):
            name = input(f"Type Player_{index} name:\n:")
            self.players[index] = Player(name, index)

    def print_table_to_console(self, next_table):
        col_string = []
        for column in range(0, 4):
            col_string.append(column)

        print(*col_string)
        row = ["A", "B", "C"]
        row_index = 0
        for table in next_table:
            print(row[row_index], *table)
            row_index += 1

    def next_round_player_steps(self, player_id):
        if self.isWinner_field:
            return

        print(f"Player: {self.players[player_id].name} round:")
        for msg in Board.menu:
            print(msg)

        step = input(">>")
        step = step.upper()

        if step == "S":
            SaveGame.save(self.table_states_collection)
            return
        if step == "L":
            SaveGame.load()
            return

        if step == "Q":
            return

        if not self.check_player_input(step):
            self.next_round_player_steps(player_id)
            return

        self.save_actual_game_state(step, player_id)

    def check_player_input(self, step):
        row_alpha_helper = ["A", "B", "C"]
        if step[0] not in row_alpha_helper:
            print("-----wrong row!-----".upper())
            return False

        if int(step[1]) not in range(1, 4):
            print("-----wrong column!-----".upper())
            return False

        return True

    def save_actual_game_state(self, step, player_id):
        """ie: step = C1 takes o or x, for player"""
        row_ = step[0]
        col_ = step[1]

        if len(self.table_states_collection) > 0:
            new_board_state = copy.deepcopy(self.table_states_collection[-1])
        else:
            new_board_state = Board.board_table

        if player_id == 0:
            marker = "o"
            new_board_state[Board.row_dict[f"{row_}"]][Board.column_dict[f"{col_}"]] = marker

        if player_id == 1:
            marker = "x"
            new_board_state[Board.row_dict[f"{row_}"]][Board.column_dict[f"{col_}"]] = marker

        self.players[player_id].add_player_step(step)
        self.print_table_to_console(new_board_state)
        self.table_states_collection.append(new_board_state)

        self.is_winner(new_board_state)

        # NEXT round
        print("--------------------")
        self.actual_player_id = 1 if self.actual_player_id == 0 else 0
        self.next_round_player_steps(self.actual_player_id)

    def is_winner(self, actual_player_board):
        # set winner table state
        if self.actual_player_id == 0:
            mark_in_row_state = ["o", "o", "o"]
        else:
            mark_in_row_state = ["x", "x", "x"]

        # region check rows:
        for row in actual_player_board:
            is_rows_equal = row == mark_in_row_state
            if is_rows_equal:
                print(f"Rows WINNER is Player_{self.actual_player_id}")
                self.isWinner_field = is_rows_equal
                break
        # endregion

        # region check columns
        for index, col in enumerate(actual_player_board[0]):
            col_one = (
                (col == "o" or col == "x")
                and col == actual_player_board[1][index]
                and col == actual_player_board[2][index]
            )
            if col_one:
                print(f"Col WINNER is Player_{self.actual_player_id}")
                self.isWinner_field = col_one
                break

        # endregion

        # region check diagonal
        # FROM TOP LEFT TO RIGHT BOTTOM
        isEqual_ltr_btn_d = (
            actual_player_board[0][0] == actual_player_board[1][1]
            and actual_player_board[1][1] == actual_player_board[2][2]
        )

        for index in range(0, 3):
            isAll_o = mark_in_row_state[0] == actual_player_board[index][index]
            # isAll_x = winner_row_state_x[0] == actual_player_board[index][index]
            if not isAll_o:
                break

        countDown = 2
        # FROM BOTTOM LEFT TO RIGHT TOP:
        for index_fom_down in range(2):
            isEqual_ltr_top_d = (
                actual_player_board[countDown][index_fom_down] == actual_player_board[countDown - 1][index_fom_down + 1]
            )
            countDown -= 1

            if not isEqual_ltr_top_d:
                break

        countDown = 2
        for index_fom_down in range(3):
            isAll_o_t = mark_in_row_state[0] == actual_player_board[countDown][index_fom_down]
            countDown -= 1
            if not isAll_o_t:
                break
        # endregion

        is_diagonal_equal = isEqual_ltr_btn_d or isEqual_ltr_top_d
        is_diagonal_O_or_X = isAll_o or isAll_o_t
        if is_diagonal_equal and is_diagonal_O_or_X:
            print(f"diag WINNER is Player_{self.actual_player_id}")
            self.isWinner = is_diagonal_equal

    def show_all_game_states():
        pass

    def reset_last_step():
        # erase last step from table_states_collection
        # actual_player_id stay!
        pass

    def save_game_to_file():
        pass


# boardMock = Board()


# region MOCK TEST:
# mockTable_row = [
# ["o","o","o"],
# ["-","-","-"],
# ["-","-","-"]]
# boardMock.is_winner(mockTable_row)

# mockTable_col = [
# ["o","-","-"],
# ["o","-","-"],
# ["-","-","-"]]
# boardMock.is_winner(mockTable_col)


# mockTable_diag_1 = [
# ["o","-","-"],
# ["-","o","-"],
# ["-","-","o"]]
# boardMock.is_winner(mockTable_diag_1)

# mockTable_diag_2 = [
# ["-","-","o"],
# ["-","o","-"],
# ["o","-","-"]]
# boardMock.is_winner(mockTable_diag_2)

# endregion
