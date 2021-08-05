# Bruno Gianesi N°USP: 10308822
# Leonardo Masson N°USP: 9267449
# Gabriel Scarabelli N° USP: 10308930

# Programa criado para o cliente que está na placa conectar e trocar mensagens

import socket as Soc

HOST = '127.0.0.1'  # IP do host (colocar IP do pc do lab)
PORT = 1234        # Porta para o cliente conectar

#Classe que cuida das funcoes do server
class Server():
        def __init__(self, ip_host: str, port: int):
                self.start_socket(ip_host, port)

        def start_socket(self, ip_host: str, port: int): #Estabelece a conexão com o ip e port oferecidos
                with Soc.socket(Soc.AF_INET, Soc.SOCK_STREAM) as socket:
                        socket.bind((ip_host, port))
                        print('Esperando a conexão do Cliente...')
                        socket.listen()
                        self.socket_connection, addr = socket.accept()
                        print('Conectado de: ' + str(addr))

        def send_message(self, message: str): #Envia a mensagem que recebeu como parâmetro
                try:
                        self.socket_connection.sendall(message.encode()) 
                except:
                        print('não foi possível enviar a mensagem')

        def receive_message(self): #Retorna a mensagem recebida pelo cliente
                return self.socket_connection.recv(1024).decode('UTF-8')

if __name__ == "__main__":
    servidor = Server(HOST,PORT)
    while True:
        #Recebe a mensagem do cliente e da print
        data = servidor.receive_message()
        print('O cliente enviou (' + data + ')')

        #Recebe a mensagem do user e envia ao cliente
        MsgSend = input("Escreva a mensagem a ser enviada ao Cliente: ")
        servidor.send_message(MsgSend)
        print('Enviado, esperando a resposta \n')

        #Caso o cliente corte a conexão, esse if detecta
        if not data:
            print ('Conexao desligada pelo cliente')
            break