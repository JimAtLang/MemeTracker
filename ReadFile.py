def readfile():
    f = open("log.txt", "r")
    lines = f.readlines()
    f.close()
    return lines