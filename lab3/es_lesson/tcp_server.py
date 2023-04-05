from socket import *

if __name__ == '__main__':

    vowels = ['A', 'E', 'I', 'O', 'U']
    serverPort = 60000

    tcpServerSocket = socket(AF_INET, SOCK_STREAM)
    tcpServerSocket.bind(('', serverPort))
    tcpServerSocket.listen(1)

    print("Il server è pronto per ricevere!")

    while True:

        connectionSocket, clientAddress = tcpServerSocket.accept()
        print(f"Connesso con {clientAddress}")
        msgFromClient = connectionSocket.recv(2048)
        msgFromClient = msgFromClient.decode('utf-8')

        msgFromClient = msgFromClient.upper()
        numCons = len(msgFromClient)

        for vowel in vowels:

            numCons = numCons - msgFromClient.count(vowel)

        response = (f"Il messaggio contiene {numCons} consonanti!")
        connectionSocket.send(response.encode('utf-8'))

        connectionSocket.close()