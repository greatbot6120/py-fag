from socket import *

if __name__ == '__main__':

    serverName = 'localhost'
    serverPort = 12000
    clientZOKET = socket(AF_INET, SOCK_DGRAM)
    clientZOKET.settimeout(5)

    stringCons = input("Immettere delle sacre lettere: ")

    clientZOKET.sendto(stringCons.encode('utf-8'), (serverName, serverPort))

    try:
        
        numOfCons, serverAddress = clientZOKET.recvfrom(2048)
        print(numOfCons.decode('utf-8'))

    except TimeoutError:
        
        print("Timeout scaduto, server non raggiungibile!")

    finally: 

        print("Chiusura socket...")
        clientZOKET.close()
