from socket import *

if __name__ == '__main__':

    def primeChecker(is_prime):

        if (is_prime == 0) or (is_prime == 1):

            response = "Il numero " + str(is_prime) + " NON E' un numero primo!"

            return(response)

        else:

            for index in range(2, is_prime):

                if not ((is_prime % index) == 0):

                    flag_prime = True

                else:

                    response = "Il numero " + str(num) + " NON E' un numero primo!"

                    return(response)

            response = "Il numero " + str(is_prime) + " E' un numero primo!"

            return(response)

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
        response = primeChecker(num)
        connectionSocket.send(response.encode('utf-8'))
        connectionSocket.close()



