import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            # Enviar nome do arquivo
            arquivo = input('Digite o nome do arquivo: ')
            sock.send(arquivo.encode())
            with open(arquivo, 'rb') as fyle:
                print('Iniciando...')
                while True:
                    data = fyle.read(1024)
                    if not data:
                        break
                    sock.send(data)
                print('Arquivo enviado!')

client = Client('192.168.1.18', 1112)
client.start()
