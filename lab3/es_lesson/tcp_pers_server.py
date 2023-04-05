from socket import *

if __name__ == '__main__':

    serverPort = 60000

    tcpPersSocket = socket(AF_INET, SOCK_STREAM)
    tcpPersSocket.bind(('', serverPort))
    tcpPersSocket.listen(1)

    print("Il server è pronto a ricevere!")

    while True:

        connectionSocket, clientAddress = tcpPersSocket.accept()
        print(f"Connesso con {clientAddress}")

        while True:

            msg_from_client = connectionSocket.recv(2048)
            msg_from_client = msg_from_client.decode('utf-8')

            if (msg_from_client == '.'):

                break

            connectionSocket.send((msg_from_client.upper()).encode('utf-8'))

        connectionSocket.close()