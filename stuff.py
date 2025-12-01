def import_friends(thingamabobs,users):
    temporaryaction = []
    for thingamabob in thingamabobs:
        temporaryaction = thingamabob.split(" ")
        if temporaryaction[2] == ("added"):
            for user in users:
                if user.first == temporaryaction[0] and user.last == temporaryaction[1]:
                    addfriendquestionmark = 0
                    for friend in user.friends:
                        if friend == (temporaryaction[3],temporaryaction[4]):
                            addfriendquestionmark = 1
                    if addfriendquestionmark == 0:
                        user.friends.append(temporaryaction[3],temporaryaction[4])
                if user.first == temporaryaction[3] and user.last == temporaryaction[4]:
                    addfriendquestionmark = 0
                    for friend in user.friends:
                        if friend == (temporaryaction[0],temporaryaction[1]):
                            addfriendquestionmark = 1
                    if addfriendquestionmark == 0:
                        user.friends.append(temporaryaction[0],temporaryaction[1])
#just alters users to include friends