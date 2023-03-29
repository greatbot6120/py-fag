import matplotlib.pyplot as plt
import requests

tempi = []

for _ in range(10):
    r = requests.get('https://www.google.com')
    tempi.append(r.elapsed.microseconds / 1000)

print('Tempo di risposta - MIN: ', min(tempi))
print('Tempo di risposta - MAX: ', max(tempi))
print('Tempo di risposta - AVG: ', sum(tempi) / len(tempi))     # len mi dice la lung. della lista,in questo caso 10

plt.figure()
plt.plot(tempi)
plt.ylim([0, max(tempi)])
plt.xlabel('ID richiesta')
plt.ylabel('[ms]')
plt.title('Test https://www.google.com')
plt.grid()
plt.show()


