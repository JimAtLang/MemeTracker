def import_friends(thingamabobs,users):
    temporaryactions = []
    for thingamabob in thingamabobs:
        temporaryactions.append(thingamabob.split(" "))
    for i in range(len(temporaryactions)):
        if "added" in temporaryactions[i]: #might have to add a space on the start of end of the string
            for user in users:
                 if user.first == temporaryactions[i][0] and user.last == temporaryactions[i][1]: #might cause errors because of how split works or it might not
                     addfriendquestionmark = 0
                     for friend in user.friends:
                        if friend == (temporaryactions[i][3],temporaryactions[i][4]):
                            addfriendquestionmark = 1
                        if addfriendquestionmark == 0:
                            user.friends.append(temporaryactions[i][3],temporaryactions[i][4])
                        if user.first == temporaryactions[i][3] and user.last == temporaryactions[i][4]:
                            addfriendquestionmark = 0
                        for friend in user.friends:
                            if friend == (temporaryactions[i][0],temporaryactions[i][1]):
                                addfriendquestionmark = 1
                        if addfriendquestionmark == 0:
                            user.friends.append(temporaryactions[i][0],temporaryactions[i][1])
#just alters users to include friends
#feed it posts
import_friends([
'Crystal Coleman added Joyce Gill as a friend on January 01, 2020',
'Tristan Patterson posted a Nobody at all: meme about hockey on January 05, 2020',
'Sarah Hess liked Tristan Pattersons mocking Spongebob meme about makeup on June 01, 2021',
'Matthew Brown DDS reposted Joyce Gills 4 panel comic meme about Candy Crush on June 28, 2021',
'Christopher Kelley reposted James Kellys image macro meme about oversleeping on July 24, 2021',
'Crystal Coleman liked Samuel Grimess Nobody at all: meme about dogs on September 21, 2021',
'Tristan Patterson posted a 4 panel comic meme about perfume on November 22, 2021'
],["Steve Jobs"])