import copy

class Board():
    board_table=[
        ["-","-","-"], 
        ["-","-","-"],
        ["-","-","-"]]
    
    row_dict = {"A":0, "B": 1, "C":2}
    column_dict = {"1":0, "2": 1, "3":2}

        

    def __init__(self) -> None:
        self.isWinner_field = False      
        self.actual_player_id = 1

        self.print_table_to_console(Board.board_table)
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

        if(self.isWinner_field):
            return

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
            is_rows_equal = row == winner_row_state_o or row == winner_row_state_x
            if(is_rows_equal):
                print(f"Rows WINNER is Player_{self.actual_player_id}")
                self.isWinner_field  = is_rows_equal
                break

        #check columns
        for index, col  in enumerate(actual_player_board[0]):
            col_one = (col == "o" or col == "x") and col == actual_player_board[1][index] and col == actual_player_board[2][index]
            if(col_one):
                print(f"Col WINNER is Player_{self.actual_player_id}")
                self.isWinner_field = col_one
                break

        #check diagonal
        #FROM TOP LEFT TO RIGHT BOTTOM
        isEqual_ltr_btn_d = actual_player_board[0][0]==actual_player_board[1][1] \
                            and actual_player_board[1][1]==actual_player_board[2][2]
        
        for index in range(0,3):
            isAll_o = winner_row_state_o[0] == actual_player_board[index][index]
            isAll_x = winner_row_state_x[0] == actual_player_board[index][index]
            if(isAll_o or isAll_x):
                break

        
        #FROM BOTTOM LEFT TO RIGHT TOP:
        for index_from_top, index_fom_down in enumerate(reversed(range(3)), range(3)):
            isEqual_ltr_top_d = actual_player_board[index_from_top][index_fom_down]==actual_player_board[index_from_top -1][index_fom_down + 1]
            if(not isEqual_ltr_top_d):
                break

        for index_from_top, index_fom_down in enumerate(reversed(range(3)), range(3)):
            isAll_o_t = winner_row_state_o[0] == actual_player_board[index_from_top][index_fom_down]
            isAll_x_t = winner_row_state_x[0] == actual_player_board[index_from_top][index_fom_down]


    
        # isEqual_ltr_top_d = actual_player_board[2][0]==actual_player_board[1][1] \
        #                 and actual_player_board[1][1]==actual_player_board[0][2]

        # isAll_o = winner_row_state_o[0] == actual_player_board[0][0] \
        #     and winner_row_state_o[0] == actual_player_board[1][1]\
        #     and winner_row_state_o[0] == actual_player_board[2][2] 
    
        # isAll_x = winner_row_state_x[0] == actual_player_board[0][0] \
        #     and winner_row_state_x[0] == actual_player_board[1][1]\
        #     and winner_row_state_x[0] == actual_player_board[2][2] 

        is_diagonal_equal = isEqual_ltr_btn_d or isEqual_ltr_top_d
        is_diagonal_O_or_X = isAll_o or isAll_x or isAll_o_t or isAll_x_t 
        if(is_diagonal_equal and is_diagonal_O_or_X):
            print(f"diag WINNER is Player_{self.actual_player_id}")
            self.isWinner = is_diagonal_equal

        #print winnder, finish and save game
        

    def show_all_game_states(): 
        pass 

    def reset_last_step():
        #erase last step from table_states_collection
        #actual_player_id stay!
        pass

    def save_game_to_file():
        pass
