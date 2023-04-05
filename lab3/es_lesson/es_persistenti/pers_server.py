from socket import *

if __name__ == '__main__':

    serverPort = 60000

    tcpPersWelcome = socket(AF_INET, SOCK_STREAM)
    tcpPersWelcome.bind(('', serverPort))
    tcpPersWelcome.listen(1)

    print("Il server è pronto per ricevere!")

    while True:

        connectionSocket, clientAddress = tcpPersWelcome.accept()
        print(f"Connesso con {clientAddress}")
        num = connectionSocket.recv(2048)
        num = int(num.decode('utf-8'))

        if (num == 0) and (num == 1):

            response = "Il numero " + str(num) + " NON E' un numero primo!"
            connectionSocket.send(response.encode('utf-8'))

        else:

            for index in range(2, num):

                if not ((num % index) == 0):

                    flag_prime = True

                else:

                    response = "Il numero " + str(num) + " NON E' un numero primo!"
                    connectionSocket.send(response.encode('utf-8'))
                    break

            response = "Il numero " + str(num) + " E' un numero primo!"
            connectionSocket.send(response.encode('utf-8'))

        connectionSocket.close()



