# tcpProgramming
readme
20191618 신혜은


1. Environment
 -python 3.9
 -from socket import *
 -from datetime import datetime

2. Files

-tcpClient.py 
 클라이언트 socket을 생성 후 서버에 요청하여 돌아오는 data를 출력한다.

-tcpServer.py
 서버 소켓을 생성 후 클라이언트에서 요청된 명령을 수행하고, 결과 data를 클라이언트로 전송한다.


3. Execute

tcpServer.py 실행 화면 
 1) tcpServer.py, tcpClient.py 실행

 2) tcpClient쪽에서 명령어 입력

  -get [file]
    ex) get good.html

  -head [file]
    ex) head good.html

  -put [file] [text]
    ex) put good.html <추가된 내용>

  -post [new file name] [text]
    ex) post newnew This is a new file.

 -close

4. 출력 메시지 코드
<기본 형식>
response = "\nHTTP/1.1 {header[0]} {header[1]}\n1Date: {date}\nHost: {url}\n Content-Type: text/html\n"

 - 200 ok : 정상 실행
 - 999 Command NOT FOUND : 잘못된 명령어를 입력했을 경우
  "HTTP/1.1 999 Command NOT FOUND (입력된 명령어는 존재하지 않음)"

 - 404 NOT FOUND : 명령어 입력시, 형식이 잘못되었을 경우
  "HTTP/1.1 404 NOT FOUND (입력형식이 올바르지 않음)"

 - 700 File Not Found : read할 파일이 존재하지 않을 경우
  "HTTP/1.1 700 File Not Found (파일이 존재하지 않음)"

