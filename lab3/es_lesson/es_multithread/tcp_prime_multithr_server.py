from socket import *
from threading import Thread

if __name__ == '__main__':

    def handler(connectionSocket):

        while True:

            var_prime = connectionSocket.recv(2048)
            var_prime = var_prime.decode('utf-8')

            if (var_prime == 0) or (var_prime == 1):

                response = "Il numero " + str(var_prime) + " NON E' un numero primo!"
                connectionSocket.send(response.encode('utf-8'))

            else:

                for index in range(2, var_prime):

                    if not ((var_prime % index) == 0):

                        flag_prime = True

                    else:

                        response = "Il numero " + str(var_prime) + " NON E' un numero primo!"
                        connectionSocket.send(response.encode('utf-8'))
                        break

                response = "Il numero " + str(var_prime) + " E' un numero primo!"
                connectionSocket.send(response.encode('utf-8'))

    serverPort = 60001
    tcpServerSocket = socket(AF_INET, SOCK_STREAM)
    tcpServerSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    tcpServerSocket.bind(('', serverPort))
    tcpServerSocket.listen(1)

    while True:

        print("Il server è pronto per ricevere!")
        varSocket, clientAddress = tcpServerSocket.accept()
        threadPrimes = Thread(target=handler, args=(varSocket,))
        threadPrimes.start()