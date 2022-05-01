from socket import *
from datetime import datetime

def get(connect):
    global response, host
    response = response.format(header=[200, 'ok'], date=datetime.now(), url=host)
    response += ("Content-Length: " + str(len(content)) + "\n\n" + content)
    connect.send(response.encode('utf-8'))

def head(connect):
    global response, host
    response = response.format(header=[200, 'ok'], date=datetime.now(), url=host)
    connect.send(response.encode('utf-8'))

def put(connect, file, add):
    global response
    txt = ""

    with open(file, "r") as f:
        lines = f.readlines()
    with open(file, "w") as f:
        for line in lines:
            if line.strip("\n") == "</body>":
                f.write(add)
            f.write(line)

    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            txt += line

    response = response.format(header=[200, 'ok'], date=datetime.now(), url=host)
    response += ("Content-Length: " + str(len(txt)) + "\n\n" + txt)
    connect.send(response.encode('utf-8'))

def post(connect, name, add):
    global response
    txt = ""
    filename = name + ".txt"
    with open(filename, "w") as f:
        f.write(add)

    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            txt += line

    response = response.format(header=[200, 'ok'], date=datetime.now(), url=host)
    response += ("Content-Length: " + str(len(txt)) + "\n\n" + txt)
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

recvMsg = connectionSocket.recv(1024)
decRecMsg = recvMsg.decode("utf-8")
# print("Server) receive msg: " + decRecMsg)  #test

order = decRecMsg.split()
if len(order) < 3:
    f = open(str(order[1]), 'r')
    if order[0] == "get":
        contents = f.readlines()
        content = ""
        for i in contents:
            content += i
        get(connectionSocket)
    if order[0] == "head":
        head(connectionSocket)
if len(order) > 2:
    if order[0] == "put":
        put(connectionSocket, str(order[1]), order[2])
    if order[0] == "post":
        post(connectionSocket, order[1], order[2])

else:
    response = "HTTP/1.1 404 NOT FOUND"
    connectionSocket.send(response.encode('utf-8'))





serverSocket.close()


