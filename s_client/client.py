import socket
import time
import keyboard
import json


class Client:
    def __init__(self) -> None:
        self.test_host = "127.0.0.1"
        self.port = 10000

        self.conntect_to_server()

    def conntect_to_server(self):
        message_object = {"name": "Andras"}

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.test_host, self.port))
            # client_socket.sendall(b"Client connected")

            while True:
                # ------outgoing
                user_input = input("[YOUR MESSAGE]:")
                message_object["message"] = user_input

                if user_input.lower() == "q":
                    client_socket.close()
                    break

                json_data = json.dumps(message_object)
                client_socket.sendall(bytes(json_data, encoding="utf-8"))

                # ------incoming
                # data = client_socket.recv(1024)  # STOPS WHILE Loop!!
                # print("SERVER:", data.decode("utf-8"))


Client()
