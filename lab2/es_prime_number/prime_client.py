from socket import *

if __name__ == '__main__':

    serverName = 'localhost'
    serverPort = 12000
    socketClient = socket(AF_INET, SOCK_DGRAM)    
    socketClient.settimeout(10)

    num = input("Inserire un numero intero valido: ")
    flag = num.isnumeric()
    
    while not flag:

        num = input("Inserire un numero intero valido: ")
        flag = num.isnumeric()

    socketClient.sendto(num.encode('utf-8'), (serverName, serverPort))

    try:

        is_prime, serverAddress = socketClient.recvfrom(2048)
        is_prime = is_prime.decode('utf-8')
        print(is_prime)

    except TimeoutError:

        print("Timeout scaduto: Server non raggiungibile")

    finally:
        
        print("Chiusura socket...")
        socketClient.close()












