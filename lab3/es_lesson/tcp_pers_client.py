from socket import *

if __name__ == '__main__':

    serverName = 'localhost'
    serverPort = 60000

    tcpPersSocket = socket(AF_INET, SOCK_STREAM)
    tcpPersSocket.connect((serverName, serverPort))

    while True:

        msg = input("Inserire lettera: ")
        tcpPersSocket.send(msg.encode('utf-8'))

        if (msg == '.'):

            break

        upperMsg = tcpPersSocket.recv(2048)
        print(f"Upper letter of {msg}: {upperMsg.decode('utf-8')}")

    tcpPersSocket.close()