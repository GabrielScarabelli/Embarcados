# Projeto Sistemas Embarcados
Repositório para tarefas de Sistemas Embarcados dos alunos Gabriel Scarabelli, Bruno Gianesi e Leonardo Masson

Bruno Gianesi N°USP: 10308822
Gabriel Scarabelli N° USP: 10308930
Leonardo Masson N°USP: 9267449
   
## Proposta final do projeto
A idéia é fazer com que o cliente se conecte com um servidor e que esses consigam trocar mensagens em uma especie de "echo"
### Conexão Cliente Servidor
##### Desenvolvimento do server utilizando a biblioteca socket do python pelo arquivo HostServer.py (Que será rodado local)
No caso o HOST utilizado é: 127.0.0.1 e a porta 1234
  1) Estabelece conexao com o cliente:

```
    def start_socket(self, ip_host: str, port: int): #Estabelece a conexão com o ip e port oferecidos
                with Soc.socket(Soc.AF_INET, Soc.SOCK_STREAM) as socket:
                        socket.bind((ip_host, port))
                        print('Esperando a conexão do Cliente...')
                        socket.listen()
                        self.socket_connection, addr = socket.accept()
                        print('Conectado de: ' + str(addr))
```

  2) Aguarda mensagem do client
```
   def receive_message(self):
                return self.socket_connection.recv(1024).decode('UTF-8')
```
  3) Envia nova mensagem ("eco") para o client
```
  def send_message(self, message: str):
                  try:
                          self.socket_connection.sendall(message.encode()) 
                  except:
                          print('não foi possível enviar a mensagem')
```
  4) Aqui temos o código principal com todas estas funções em uso:
```
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
```

##### No caso do cliente, conectamos ele por TCP (O programa Cliente.c sera rodado dentro da placa)
  1) Abre o socket tipo TCP
```
  	sockId = socket(AF_INET, SOCK_STREAM, 0);
    if (sockId < 0) {
      printf("Stream socket nao pode ser aberto\n");
      return(1);
    }
```
  2) Conecta o socket ao servidor
```
    connId = connect(sockId, (struct sockaddr *)&client, sizeof(client));
    if (connId == -1) {
      printf("A conexao com o servidor %s na porta %s falhou\n", argv[1], argv[2]);
      close(sockId);
      return(1);
    }
```
  3) Envio da mensagem
```
  		printf("Digite a mensagem para a aplicação do Servidor (Nao coloque barra de espaco): ");
		scanf("%s",buf);
		printf("Mensagem enviada, esperando resposta \n ");
		sentBytes = send(sockId, buf, strlen(buf), 0);
		if (sentBytes < 0) {
			close(sockId);
			printf("A conexao foi perdida\n");
			return(1);
		}
		memset(buf,0,sizeof(buf));
```
  4) Recebe as mensagens
```
  		recvBytes = recv(sockId, buf, MAX_FLOW_SIZE, 0);
		if (recvBytes < 0) {
			close(sockId);
			printf("Ocorreu um erro na aplicacao\n");
			return(1);
		}
		if (recvBytes == 0) {
			close(sockId);
			printf("A conexao foi encerrada pelo servidor\n");
			return(1);
		}
		printf("O servidor retornou %zu caracteres: [%s]\n", strlen(buf), buf);
		memset(buf,0,sizeof(buf));
```
