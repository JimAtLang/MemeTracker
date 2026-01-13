fd = {}

def get_friends():
    f = open("log.txt", "r")
    lines = f.readlines()
    friendlines = []
    friends = {}
    for line in lines:
        if "as a friend" in line:
            friendlines.append(line.strip())
    for string in friendlines:
        name1 = ""
        words = string.split()
        #this for loop gets the first name
        wordnumber = 0
        for word in words:
            wordnumber += 1
            if word != "added":
                name1 = name1 + word + " "
            else:
                break
        word = words[wordnumber]
        name2 = ""
        while word != "as":
            name2 += word + " "
            wordnumber += 1
            word = words[wordnumber]
        if not name1 in fd:
            fd[name1] = []
        if not name2 in fd[name1]:
            fd[name1].append(name2)
    return fd