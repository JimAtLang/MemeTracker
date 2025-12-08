def dataToUsers(strings):
    users=[]
    for s in strings:
        for user in users:
            if s.split(" ")[0]==user.firstName and s.split(" ")[1]==user.lastName:
                if s.split(" ")[3]=="added":
                    //do some stuff
                if s.split(" ")[3]=="posted":
                    b=s.split(" ")
                    del b[:3]
                    u.posts.append("".join(b))
                if s.split(" ")[3]=="liked":
                    //do some stuff
//this stuff is when it misses everything
u:User=none
u.firstName=s.split(" ")[0]
u.firstName=s.split(" ")[1]