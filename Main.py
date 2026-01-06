<<<<<<< HEAD
f = open("log.txt", "r")

lines = f.readlines()
edited = []
for line in lines:
    if "reposted" in line:
        edited.append("[3] " + line)
        continue
    if "as a friend" in line:
        edited.append("[2] " + line)
        continue
    if "posted" in line:
        edited.append("[1] " + line)
    if "liked" in line:
        edited.append("[4] " + line)
new = open("new.txt", "w")
new.writelines(edited)
=======
>>>>>>> 22f2fc8fc111ef1ad4daf705c7eff0cdff2e24e3
