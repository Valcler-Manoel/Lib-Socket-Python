import socket


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.host, self.port))
            print('Socket criado!')
            sock.listen(5)
            print('Esperando conexão...')
            conn, addr = sock.accept()
            with conn:
                print('Nova conexão de', addr, '!')
                arquivo = conn.recv(1024).decode()
                with open(arquivo, 'wb') as fyle:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        fyle.write(data)
                    print(f'Arquivo {arquivo} recebido!')


server = Server('', 1112)
server.start()
