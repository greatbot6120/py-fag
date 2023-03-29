if __name__ == '__main__':

    firstWebsite = "https://google.com"
    secondWebsite = "https://netflix.com"

    slicedManual = firstWebsite[0:8:]
    slicedWeb = slice(7, -4)
    print(firstWebsite[slice(7, -4)])
    print(slicedManual)
