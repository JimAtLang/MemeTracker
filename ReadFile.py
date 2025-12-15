def readfile():
    f = open("file.txt", "r")
    lines = f.readlines()
    f.close()
    return lines