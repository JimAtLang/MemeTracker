from User import User

def dataToUsers(strings):
    users=[]
    for s in strings:
        for user in users:
            u:User=None
            if s.split(" ")[0]==user.firstName and s.split(" ")[1]==user.lastName:
                #if s.split(" ")[3]=="added":
                    #do some stuff
                if s.split(" ")[3]=="posted": #just a temp post thing, will link to an object later
                    b=s.split(" ")
                    del b[:3]
                    u.posts.append("".join(b))
                #if s.split(" ")[3]=="liked":
                    #do some stuff
                continue
            #this stuff is when it misses everything
            u:User=None
            u.firstName=s.split(" ")[0]
            u.firstName=s.split(" ")[1]
            print("first"+u.firstName)
            print("last"+u.lastName)
            print("posts"+u.posts)