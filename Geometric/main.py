from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)  # 서버 소켓 생성
serverPort = 7777
serverSocket.bind(('', serverPort))  # 서버 주소와 포트 넘버 바인드
serverSocket.listen(1)  # 1개의 connection 가능, 웹 서버 동작(소켓 동작)

while True:
    print('The server is ready to receive')
    connectionSocket, addr = serverSocket.accept()  # 클라이언트에서 요청 연결이 들어오면 connection 소켓 생성

    try:
        message = connectionSocket.recv(2048).decode()  # 클라이언트에서 요청 메시지를 받음, 8비트 바이너리를 7비트 아스키로 변환
        print(message)

        filename = message.split()[1]  # 메시지에서 경로 추출, URL값 가져
        print(filename)

        myfile = open(filename[1:], 'rb')  # /를 제외한 나머지 읽

        response = myfile.read()
        myfile.close()

        header = 'HTTP/1.1 200 OK\n'

        if (filename.endswith(".jpg")):
            filetype = 'image/jpg'
        elif (filename.endswith(".gif")):
            filetype = 'image/gif'
        elif (filename.endswith(".mp4")):
            filetype = 'video/mp4'
        elif (filename.endswith(".wmv")):
            filetype = 'video/wmv'
        else:
            filetype = 'text/html'

        header += 'Content-Type: ' + str(filetype) + '\n\n'
        print(header)

        connectionSocket.send(header.encode())  # 다시 바이너리로 인코딩함
        connectionSocket.send(response)
        connectionSocket.close()

    except IOError:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode()

        print(header)
        connectionSocket.send(header.encode())
        connectionSocket.send(response)
        connectionSocket.close()

serverSocket.close()
sys.exit()
