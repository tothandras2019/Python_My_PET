import socket
import json


class Client:
    def __init__(self, player_instance=None) -> None:
        self.test_host = "127.0.0.1"
        self.port = 10000

        # self.conntect_to_server()

    def conntect_to_server(self) -> None:
        message_object = {"player": self.player.name}

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            server_address = (self.test_host, self.port)
            client_socket.connect(server_address)
            # client_socket.sendall(b"Client connected")

            while True:
                # ------outgoing
                user_input = input("[YOUR MESSAGE]:")
                message_object["step"] = user_input

                if user_input.lower() == "q":
                    client_socket.close()
                    break

                json_data = json.dumps(message_object)
                client_socket.sendto(bytes(json_data, encoding="utf-8"), server_address)

                # ------incoming
                data = client_socket.recv(1024)  # STOPS WHILE Loop!!
                print("SERVER:", data.decode("utf-8"))


# Client()
