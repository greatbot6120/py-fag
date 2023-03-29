import requests

def media(avrDelays):
    
    return(sum(avrDelays) / len(avrDelays))

webAddresses = ['http://www.google.com',
                'http://www.youtube.com',
                'http://www.polimi.it',
                'http://www.wikipedia.org',
                'http://www.twitter.com']

totalAvrs = []

for url in webAddresses:

    delays = []

    for _ in range(10):

        req = requests.get(url)
        delays.append(req.elapsed.microseconds / 1000)
    
    print("Tempi per:", url, delays)
    totalAvrs.append(media(delays))

mediaMin = min(totalAvrs)

for indexLoop in range(len(totalAvrs)):

    if (totalAvrs[indexLoop] == mediaMin):

        print(f"il tempo medio migliore è quello di {webAddresses[indexLoop]}: {mediaMin}")

#print(totalAvrs)




