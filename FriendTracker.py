f = open("log.txt", "r")
lines = f.readlines()
friends = []
for line in lines:
    if "as a friend" in line:
        friends.append(line.strip())
print(friends)
name = ""
for string in friends:
    words = string.split()
    for word in words:
        if word != "added":
            name = name + word + " "
        else:
            break
print(name)