from socket import *

if __name__ == '__main__':

    vocals = ['A', 'E', 'I', 'O', 'U']

    msgNumber = 1
    serverPort = 12000
    serverZOKET = socket(AF_INET, SOCK_DGRAM)
    serverZOKET.bind(('', serverPort))

    print("Il server è pronto per ricevere")

    while True:

        message, clientAddress = serverZOKET.recvfrom(2048)
        print(f"{msgNumber}° messaggio ricevuto da: {clientAddress}")
        message = message.decode('utf-8')
        message = message.upper()
        numCons = len(message)
        
        for vocal in vocals:

            numCons = numCons - message.count(vocal)

        response = (f"Il messaggio contiene {numCons} consonanti!")
        serverZOKET.sendto(response.encode('utf-8'), clientAddress)
        msgNumber = msgNumber + 1
