import socket
import time
import json


class Server:
    def __init__(self) -> None:
        self.test_host = "127.0.0.1"
        self.port = 10000

        self.start()

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.test_host, self.port))
            s.listen(1)

            print("Server wait")

            conn, addr = s.accept()
            try:
                with conn:
                    print("Connected:", addr)
                    while True:
                        # ----incoming
                        data = conn.recv(1024)  # STOPS WHILE Loop!!

                        if len(data) <= 0:
                            print("Disconected!")
                            break

                        rec_data = data.decode("utf-8")
                        json_data = json.loads(rec_data)
                        print(f"[MSG FROM {addr}]:", json_data["name"], json_data["message"])

                        # ----outgoing
                        ack = json.dumps("Got it from")
                        conn.sendall(bytes(ack, encoding="utf-8"))
            except ConnectionResetError as err:
                print("[err]:", err)


Server()
