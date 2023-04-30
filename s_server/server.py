import socket
import time
import json
import threading


class Server:
    def __init__(self) -> None:
        self.test_host = "127.0.0.1"
        self.port = 10000
        self.isWait = True
        self.clients={}

        self.start()

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.test_host, self.port))
            s.listen(5)

            sockname = s.getsockname()
            print(f"Server started on host:{sockname[0]}:{sockname[1]}")
            wait_trhead = threading.Thread(target=self.waiting_signal, daemon=True)
            while True:
                wait_trhead.start()
                client_connection, cliend_address = s.accept()

                if cliend_address:
                    self.isWait = False

                try:
                    with client_connection:
                        print("\nConnected:", cliend_address)

                        while True:
                            # ----incoming
                            data = client_connection.recv(1024)  # STOPS WHILE Loop!!

                            if len(data) <= 0:
                                raise RuntimeError(f"{cliend_address} disconected!")

                            rec_data = data.decode("utf-8")
                            json_data = json.loads(rec_data)

                            print(f"[MSG FROM {cliend_address}]:", json_data["name"], json_data["message"])

                            # ----outgoing
                            ack = json.dumps(f"[MSG from {cliend_address}]:{json_data['message']}")
                            client_connection.sendall(bytes(ack, encoding="utf-8"))

                except ConnectionResetError as err:
                    print("[err]:", err)
                except Exception as e:
                    print("Connection lost!")
                finally:
                    client_connection.close()
                    break

    def waiting_signal(self):
        print(f"Wait for clients", end="")
        while self.isWait:
            print(f".", end="")
            time.sleep(1)


Server()

# NOTE:
# These are buffered “files”, and a common mistake is to write something, and then read for a reply. Without a flush in there, you may wait forever for the reply, because the request may still be in your output buffer.
