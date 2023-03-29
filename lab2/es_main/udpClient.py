from socket import *

if __name__ == '__main__':

    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    
    msgClient = input("Inserisci qui il tuo messaggio al server: ")
    
    # Codifica messaggio ed invio al server
    clientSocket.sendto(msgClient.encode('utf-8'), (serverName, serverPort))

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    modifiedMessage = modifiedMessage.decode('utf-8')
    print(modifiedMessage)

    clientSocket.close()
