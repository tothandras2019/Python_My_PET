from TicTacToe import Board

# path = os.getcwd()
# html_file=os.path.join("file:///", path,"index.html" )
# print(html_file)

# louncher = webbrowser.get()
# print(louncher)
# louncher.open(html_file, 1, True)

class Main():
    activity=["1) Tic-Tack-Toe", "2) Any URL loader", "Q) EXIT"]

    def __init__(self) -> None:
        self.choose_task()
        pass

    def choose_task(self):
        user_input = ''
        while user_input!='Q':
            print("[MAIN]:Válasszon!\n", *Main.activity)
            user_input=input().upper()
            match (user_input):
                case "Q":
                    print('TERMINATE')
                case "1":
                    print("Tic Tac Toe Start")
                    Board()   
                case "2":
                    print("Any URL loader")
    
    
Main()
