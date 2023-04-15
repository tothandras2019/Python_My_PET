import copy

class Board():
    board_table=[
        ["-","-","-"], 
        ["-","-","-"],
        ["-","-","-"]]
    
    row_dict = {"A":0, "B": 1, "C":2}
    column_dict = {"1":0, "2": 1, "3":2}

        

    def __init__(self) -> None:
        self.print_table_to_console(Board.board_table)
        self.actual_player_id = 1
        self.table_states_collection=[Board.board_table]
        self.next_round_player_steps(self.actual_player_id)        
        pass

    def print_table_to_console(self, next_table):
        col_string=[]
        for column in range(0, 4):
            col_string.append(column)
        
        print(*col_string)
        row=["A", "B", "C"]
        row_index=0
        for table in next_table:
            print(row[row_index], *table)
            row_index += 1

    def next_round_player_steps(self, player_id):
        print(f'Player_{player_id} round:')
        step = input("#Type field (example: A3+enter)\n#Quit type Q+enter\n")
        if(step.upper()=="Q"):
            return
        
        if(not self.check_player_input(step)):
            self.next_round_player_steps(player_id)
            return

        self.save_actual_state(step, player_id)

    def check_player_input(self, step):
        row_alpha_helper=["A", "B", "C"]
        if(step[0] not in row_alpha_helper ):
            print("-----wrong row!-----".upper())
            return False
        
        if(int(step[1]) not in range(1,4)):
            print("-----wrong column!-----".upper())
            return False
        
        return True

    def save_actual_state(self, step, player_id):
        '''ie: step = C1 takes o or x, for player'''
        row_= step[0]
        col_= step[1]

        print("ROW/COL",row_, col_)
        new_board_state= copy.deepcopy(self.table_states_collection[-1])

        if(player_id==1):
            marker="o"
            new_board_state[Board.row_dict[f'{row_}']][Board.column_dict[f'{col_}']]=marker
            
        if(player_id==2):
            marker="x"
            new_board_state[Board.row_dict[f'{row_}']][Board.column_dict[f'{col_}']]=marker

        self.print_table_to_console(new_board_state)
        self.table_states_collection.append(new_board_state)
        self.is_winner(new_board_state)

        #NEXT round
        print("--------------------")
        self.actual_player_id = 2 if self.actual_player_id==1 else 1
        self.next_round_player_steps(self.actual_player_id)  

    def is_winner(self, actual_player_board):
        #set winner table state

        #check rows:
        winner_row_state_o=["o","o","o"]
        winner_row_state_x=["x","x","x"]

        for row in actual_player_board:
            if(row == winner_row_state_o or row == winner_row_state_x):
                print(f"WINNER is Player_{self.actual_player_id}")

        #TODO:check columns

        #TODO:check diagonal

        #print winnder, finish and save game
        pass

    def show_all_game_states(): 
        pass 

    def reset_last_step():
        #erase last step from table_states_collection
        #actual_player_id stay!
        pass

    def save_game_to_file():
        pass