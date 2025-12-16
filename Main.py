from User import User
from Post import Post

f = open("log.txt", "r")
lines = f.readlines()
edited = []
for line in lines:
    if "liked" in line:
        edited.append("[4] " + line)
    if "reposted" in line:
        edited.append("[3] " + line)
    if "as a friend" in line:
        edited.append("[2] " + line)
    if "posted" in line:
        edited.append("[1] " + line)

new = open("new.txt", "w")
new.writelines(edited)
