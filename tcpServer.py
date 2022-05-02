from socket import *
from datetime import datetime

def get(connect, file):
    global response, host

    try:
        f = open(file, 'r')     #요청된 파일 open
        contents = f.readlines()
        content = ""
        for i in contents:
            content += i    #파일 내용을 string으로 받기

        response = response.format(header=[200, 'ok'], date=datetime.now(), url=host)   #응답 메시지
        response += ("Content-Length: " + str(len(content)) + "\n\n" + content) #파일 내용의 length와 내용 출력
    except FileNotFoundError as e:
        response = ("\nHTTP/1.1 700 File Not Found\n(파일이 존재하지 않음)") #파일이 존재하지 않는 예외 처리

    connect.send(response.encode('utf-8'))  #응답메시지를 client로 전송


def head(connect, file):
    global response, host

    try:
        f = open(file, 'r')
        contents = f.readlines()
        content = ""
        for i in contents:
            content += i    #파일에 있는 내용 string으로 받기

        response = response.format(header=[200, 'ok'], date=datetime.now(), url=host)
    except FileNotFoundError:
        response = ("\nHTTP/1.1 700 File Not Found\n(파일이 존재하지 않음)")

    connect.send(response.encode('utf-8'))

def put(connect, file, add):
    global response
    txt = ""
    tag = "</body>"     #body 태그를 수정

    try:
        with open(file, "r") as f:
            lines = f.readlines()
        with open(file, "w") as f:
            for line in lines:
                if line.strip("\n") == tag:     #tag를 만나면 add 작성
                    f.write("\t" + add + "\n\n")
                f.write(line)

        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                txt += line     #add가 추가된 파일내용 string 값으로 받기

        response = response.format(header=[200, 'ok'], date=datetime.now(), url=host)
        response += ("Content-Length: " + str(len(txt)) + "\n\n" + txt)
    except FileNotFoundError:
        response = ("\nHTTP/1.1 700 File Not Found\n(파일이 존재하지 않음)")

    connect.send(response.encode('utf-8'))

def post(connect, name, add):
    global response
    txt = ""
    filename = name + ".html"

    try:
        with open(filename, "w") as f:
            f.write(add)        #새로운 파일을 생성하고, 내용에 add 값을 추가

        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                txt += line     #생성된 파일 내용을 string값으로 받기

        response = response.format(header=[200, 'ok'], date=datetime.now(), url=host)
        response += ("Content-Length: " + str(len(txt)) + "\n\n" + txt)
    except FileNotFoundError:
        response = ("\nHTTP/1.1 700 File Not Found\n(파일이 존재하지 않음)")

    connect.send(response.encode('utf-8'))

host = "127.0.0.1"
port = 12345
response = "\nHTTP/1.1 {header[0]} {header[1]}\n1Date: {date}\nHost: {url}\n" \
           "Content-Type: text/html\n"
cmdList = ["get", "head", "put", "post", "close"]

serverSocket = socket(AF_INET, SOCK_STREAM)     #server 소켓 생성
serverSocket.bind((host, port))
serverSocket.listen(1)
print("------------Server) 대기중------------")

connectionSocket, addr = serverSocket.accept()

recvMsg = connectionSocket.recv(1024)       #Client로부터 request 받기
decRecMsg = recvMsg.decode("utf-8")

order = decRecMsg.split()   #입력된 메시지를 공백을 기준으로 split하여 리스트로 저장
try:
    if order[0] not in cmdList:     #명령어가 아닌 다른 단어가 입력되었을 경우
        response = "\nHTTP/1.1 999 Command NOT FOUND\n(입력된 명령어는 존재하지 않음)" #999 에러발생
        connectionSocket.send(response.encode('utf-8'))
        serverSocket.close()
    else:
        if order[0] == "close":     #close 입력시 소켓 종료
            serverSocket.close()
            print("Server) Good Bye")
        elif order[0] == "get":
            get(connectionSocket, order[1])
        elif order[0] == "head":
            head(connectionSocket, order[1])
        elif order[0] == "put":
            put(connectionSocket, order[1], " ".join(str(i) for i in order[2:]))
        elif order[0] == "post":
            post(connectionSocket, order[1], " ".join(str(i) for i in order[2:]))

except IndexError:
    response = "\nHTTP/1.1 404 NOT FOUND\n(입력형식이 올바르지 않음)"
    connectionSocket.send(response.encode('utf-8'))

print("------------Server) 전송함------------")
serverSocket.close()





