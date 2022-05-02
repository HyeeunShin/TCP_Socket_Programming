from socket import *

ip ="127.0.0.1"
port = 12345

clientSocket = socket(AF_INET, SOCK_STREAM)  #client 소켓 생성
clientSocket.connect((ip, port))    #소켓 연결
print("------------Client) 연결됨------------")

inputMsg = input("Request: ")   #명령어 입력
clientSocket.send(inputMsg.encode("utf-8"))     #입력된 명령을 Server로 전송
print("-----------Client) 전송완료------------")

data = clientSocket.recv(1024)  #서버로부터 데이터 전달받기
print(data.decode("utf-8"))

clientSocket.close()
print("\n------------Client) 종료함------------")
