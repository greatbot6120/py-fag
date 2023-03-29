import requests

if __name__ == '__main__':
    
    sites = ['https://www.google.com', 'https://www.youtube.com']
    avrDelays = []

    for numSite in sites:

        delays = []
        
        for _ in range(5):

            req = requests.get(numSite)
            delays.append(req.elapsed.microseconds / 1000)
        
        print(delays)
        print(f"AVR delay of {numSite} = {sum(delays) / len(delays)}")
        avrDelays.append(sum(delays) / len(delays))

    if avrDelays[0]  > avrDelays[1]:
        
        print(f"The best average response time is {avrDelays[0]} of the site {sites[0]}")
    
    else:

        print(f"The best average response time is {avrDelays[1]} of the site {sites[1]}")

