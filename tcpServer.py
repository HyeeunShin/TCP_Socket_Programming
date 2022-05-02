from socket import *
from datetime import datetime

def get(connect, file):
    global response, host

    f = open(file, 'r')
    contents = f.readlines()
    content = ""
    for i in contents:
        content += i

    response = response.format(header=[200, 'ok'], date=datetime.now(), url=host)
    response += ("Content-Length: " + str(len(content)) + "\n\n" + content)
    connect.send(response.encode('utf-8'))

def head(connect, file):
    global response, host

    f = open(file, 'r')
    contents = f.readlines()
    content = ""
    for i in contents:
        content += i

    response = response.format(header=[200, 'ok'], date=datetime.now(), url=host)
    connect.send(response.encode('utf-8'))

def put(connect, file, add):
    global response
    txt = ""
    tag = "</body>"

    with open(file, "r") as f:
        lines = f.readlines()
    with open(file, "w") as f:
        for line in lines:
            if line.strip("\n") == tag:
                f.write("\t" + add + "\n\n")
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
response = "HTTP/1.1 {header[0]} {header[1]}\n1Date: {date}\nHost: {url}\n" \
           "Content-Type: text/html\n"

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(1)
print("Server) 대기중")

connectionSocket, addr = serverSocket.accept()

recvMsg = connectionSocket.recv(1024)
decRecMsg = recvMsg.decode("utf-8")

order = decRecMsg.split()

try:
        if order[0] == "get":
            get(connectionSocket, order[1])
        elif order[0] == "head":
            head(connectionSocket, order[1])
        elif order[0] == "put":
            put(connectionSocket, order[1], order[2])
        elif order[0] == "post":
            post(connectionSocket, order[1], order[2])
        elif order[0] == "close":
            serverSocket.close()
            print("Server) Good Bye")
        else:
            response = "HTTP/1.1 999 NOT FOUND\n(입력된 명령어는 존재하지 않음)"
            connectionSocket.send(response.encode('utf-8'))

except IndexError:
    response = "HTTP/1.1 404 NOT FOUND\n(입력형식이 올바르지 않음)"
    connectionSocket.send(response.encode('utf-8'))

print("Server) 전송 완료")





