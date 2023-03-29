import requests
import matplotlib.pyplot as plt

m = 0   # massimo tra i massimi
plt.figure()

siti = ['http://www.gazzetta.it', 'http://www.netflix.com', 'http://www.facebook.com']
stili = ['--', '-.', ':']
for url, stile in zip(siti, stili):
    print('Test', url)
    tempi = []
    for _ in range(10):
        r = requests.get(url)
        tempi.append(r.elapsed.microseconds / 1000)
    plt.plot(tempi, label=url, linestyle=stile)
    print('Tempo di risposta - MIN: ', min(tempi), 'ms')
    print('Tempo di risposta - MAX: ', max(tempi), 'ms')
    print('Tempo di risposta - AVG: ', sum(tempi)/len(tempi), 'ms')
    m = max([m, max(tempi)])    # ricalcolo il massimo tra i massimi

plt.ylim([0, 1.1*m])
plt.xlabel('ID richiesta')
plt.ylabel('[ms]')
plt.title('Test tempi di risposta')
plt.legend(loc='upper right', fontsize=8)
plt.grid()
plt.show()
