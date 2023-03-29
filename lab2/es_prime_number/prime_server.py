from socket import *

if __name__ == '__main__':
    
    flag_prime = None
    response = None
    msgCounter = 1
    serverPort = 12000
    socketServer = socket(AF_INET, SOCK_DGRAM)
    socketServer.bind(('', serverPort))

    print("Il server è pronto per ricevere: ")

    while True:

        num, clientAddress = socketServer.recvfrom(2048)
        print(f"{msgCounter}° messaggio da {clientAddress}")
        num = num.decode('utf-8')
        num = int(num)
    
        if (num == 0) and (num == 1):
            
            response = "Il numero " + str(num) + " NON E' un numero primo!" 
            socketServer.sendto(response.encode('utf-8'), clientAddress)
        
        else:

            for index in range(2, num):

                if not ((num % index) == 0):
                
                    flag_prime = True

                else:
                    
                    response = "Il numero " + str(num) + " NON E' un numero primo!"
                    socketServer.sendto(response.encode('utf-8'), clientAddress)
                    break
            
            
            response = "Il numero " + str(num) + " E' un numero primo!"
            socketServer.sendto(response.encode('utf-8'), clientAddress)

        msgCounter = msgCounter + 1 






             
            
