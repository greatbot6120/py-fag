import requests

if __name__ == '__main__':
    for i in range(10):  # se metto _  non mi interessa tenere conto del numero di iterazioni
        r = requests.get('https://www.google.com')
        print('Tempo di risposta ', i+1, ': ', r.elapsed.microseconds / 1000, 'ms')
