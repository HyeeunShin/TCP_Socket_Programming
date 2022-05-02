# tcpProgramming
# 2022_1_Computer_Network

국민대학교 소프트웨어학부 20191618 신혜은

# Description
TCP 기반 소켓프로그래밍
   Client에서는 HTTP 프로토콜의 GET/HEAD/POST/PUT Request를 요청하고
   Server에서는 Client의 Request에 따라 응답 메시지를 구성하여 Response하도록 구현
   * 예) Method-응답 xxx의 case 5개 이상 수행.
      GET-응답 4xx, GET-응답 2xxx, HEAD-응답 1xx, POST-응답 2xxx, POST-응답 1xx 등
   * 소켓 통신은 PC가 2대 이상이면 Client, Server 실행은 분리하여 진행
      2대 이상 환경이 안되는 경우는 localhost로 진행도 가능
      
# 1. Environment

      -python 3.9
      -from socket import *
      -from datetime import datetime

# 2. Files
-tcpClient.py 
 클라이언트 socket을 생성 후 서버에 요청하여 돌아오는 data를 출력한다.

-tcpServer.py
 서버 소켓을 생성 후 클라이언트에서 요청된 명령을 수행하고, 결과 data를 클라이언트로 전송한다.


# 3. Execute
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
3) 결과 확인

# 4. Response State

<기본 형식>
   response = "\nHTTP/1.1 {header[0]} {header[1]}\n1Date: {date}\nHost: {url}\n Content-Type: text/html\n"

 - 200 ok : 정상 실행
 
 - 999 Command NOT FOUND : 잘못된 명령어를 입력했을 경우
  "HTTP/1.1 999 Command NOT FOUND (입력된 명령어는 존재하지 않음)"

 - 404 NOT FOUND : 명령어 입력시, 형식이 잘못되었을 경우
  "HTTP/1.1 404 NOT FOUND (입력형식이 올바르지 않음)"

 - 700 File Not Found : read할 파일이 존재하지 않을 경우
  "HTTP/1.1 700 File Not Found (파일이 존재하지 않음)"

