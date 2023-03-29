import requests

medio = []

siti = ['http://google.com', 'http://www.youtube.com', 'http://www.netflix.com']

for url in siti:
    print('Test', url)
    tempi = []
    for _ in range(5):
        r = requests.get(url)
        tempi.append(r.elapsed.microseconds / 1000)
    media = sum(tempi) / len(tempi)
    print('La media di ', url, 'è: ', media)
    medio.append(media)

minimo = medio[0]

for url in range(len(siti)):
    if medio[url] <= minimo:
        minimo = medio[url]

for i in range(len(medio)):
    if minimo == medio[i]:
        print(siti[i])
