from socket import *
from datetime import datetime
import sys

import os
import mySocket
def get(connect):
    global response, host
    response = response.format(header=[200, 'ok'], date=datetime.now(), url=host)
    response += ("Content-Length:\n" + len(content) + "\n" + content)
    connect.send(response.encode('utf-8'))

def head(connect):
    global response, host
    response = response.format(header=[200, 'ok'], date=datetime.now(), url=host)
    connect.send(response.encode('utf-8'))

host = "127.0.0.1"
port = 12345
response = "HTTP/1.1 {header[0]} {header[1]}\nDate: {date}\nHost: {url}\n" \
           "Content-Type: text/html\n"


serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(1)
print("Server) 대기중")

connectionSocket, addr = serverSocket.accept()

#print(str(addr), "server에서 접속되었습니다.")

recvMsg = connectionSocket.recv(1024)
decRecMsg = recvMsg.decode("utf-8")
print("Receive msg: " + decRecMsg)  #test

order = decRecMsg.split()
if len(order) > 1:
    f = open(str(order[1]), 'r')
    if order[0] == "get":
        contents = f.readlines()
        content = ""
        for i in contents:
            content += i
        get(connectionSocket)
    if order[0] == "head":
        head(connectionSocket)

else:
    response = "HTTP/1.1 404 NOT FOUND"
    connectionSocket.send(response.encode('utf-8'))





serverSocket.close()


