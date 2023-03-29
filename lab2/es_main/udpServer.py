from socket import *

if __name__ == '__main__':
   
    msgNumber = 1
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))

    print("Il server è pronto per ricevere:")

    while True:

        message, clientAddress = serverSocket.recvfrom(2048)
        print(f"{msgNumber}° messaggio ricevuto da: {clientAddress}")
        modifiedMessage = message.decode('utf-8')
        modifiedMessage = modifiedMessage.upper()
        serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)
        msgNumber = msgNumber + 1 
