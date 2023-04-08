from socket import *
from threading import Thread

if __name__ == '__main__':

    def handler(connectionSocket):

        while True:

            flag_prime = True
            var_prime = connectionSocket.recv(2048)
            var_prime = var_prime.decode('utf-8')
            var_prime = int(var_prime)

            if var_prime > 2:

                for index in range(2, var_prime):

                    if (var_prime % index) == 0:

                        flag_prime = False
                        break

            if flag_prime:

                response = "Il numero " + str(var_prime) + " E' un numero primo!"
                connectionSocket.send(response.encode('utf-8'))

            else:

                response = "Il numero " + str(var_prime) + " NON E' un numero primo!"
                connectionSocket.send(response.encode('utf-8'))

    serverPort = 60001
    tcpServerSocket = socket(AF_INET, SOCK_STREAM)
    tcpServerSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    tcpServerSocket.bind(('', serverPort))
    tcpServerSocket.listen(1)
    print("Il server è pronto per ricevere!")

    while True:

        varSocket, clientAddress = tcpServerSocket.accept()
        print(f"Connessione da: {clientAddress}")
        threadPrimes = Thread(target=handler, args=(varSocket,))
        threadPrimes.start()