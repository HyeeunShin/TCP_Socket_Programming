from socket import *

ip ="127.0.0.1"
port = 12345 #http port number : 80


clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((ip, port))
print("Client) 연결됨")

inputMsg = input("Request: ")
clientSocket.send(inputMsg.encode("utf-8"))
print("Client) 전송 완료")

data = clientSocket.recv(1024)
print(data.decode("utf-8"))

clientSocket.close()
