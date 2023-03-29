from socket import *

if __name__ == '__main__':

    serverName = 'localhost'

    # Porta errata
    serverPort = 12001
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    # Timeout socket
    clientSocket.settimeout(5)
    msgClient = input("Inserisci qui il tuo messaggio al server: ")
    
    # Codifica messaggio ed invio al server
    clientSocket.sendto(msgClient.encode('utf-8'), (serverName, serverPort))
    
    # Error handling
    try:

        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifiedMessage.decode('utf-8'))

    except TimeoutError:

        print("Timeout scaduto: Server non raggiungibile!")
    
    finally:

        print("Chiusura socket...")
        clientSocket.close()
