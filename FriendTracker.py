def get_friends():
    f = open("log.txt", "r")
    lines = f.readlines()
    friendlines = []
    friends = []
    for line in lines:
        if "as a friend" in line:
            friendlines.append(line.strip())
    for string in friendlines:
        name = ""
        words = string.split()
        for word in words:
            if word != "added":
                name = name + word + " "
            else:
                break
        if name not in friends:
            friends.append(name)
    return friends