from socket import *

if __name__ == '__main__':

    serverName = 'localhost'
    serverPort = 60000

    tcpClientSocket = socket(AF_INET, SOCK_STREAM)
    tcpClientSocket.connect((serverName, serverPort))

    msg = input("Inserire holy phrase: ")
    tcpClientSocket.send(msg.encode('utf-8'))

    msgFromServer = tcpClientSocket.recv(2048)
    print(msgFromServer.decode('utf-8'))

    tcpClientSocket.close()
