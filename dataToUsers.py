from User import User

def dataToUsers(strings:list[str]):
    users=[]
    for s in strings:
        for user in users:
            u=user
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
        u = User("", s.split(" ")[0], s.split(" ")[1])
        users.append(u)
        # print("first"+u.firstName)
        # print("last"+u.lastName)
    return users