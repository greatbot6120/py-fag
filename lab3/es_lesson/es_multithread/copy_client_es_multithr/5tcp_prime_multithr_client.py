from socket import *

if __name__ == '__main__':

    serverName = 'localhost'
    serverPort = 60001

    tcpPersSocket = socket(AF_INET, SOCK_STREAM)
    tcpPersSocket.connect((serverName, serverPort))
    tcpPersSocket.settimeout(10)

    numClient = input("Inserire l'Holy number versione multithreading: ")
    tcpPersSocket.send(numClient.encode('utf-8'))

    try:

        is_prime = tcpPersSocket.recv(2048)
        print(is_prime.decode('utf-8'))

    except TimeoutError:

        print("Timeout scaduto, Server non raggiungibile!")

    finally:

        print("Chiusura socket...")
        tcpPersSocket.close()
