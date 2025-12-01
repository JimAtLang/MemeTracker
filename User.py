import datetime

class User:
    def __init__(self, posts, firstName:str="", lastName:str="", joinDate:datetime="", friends=""):
        self.firstName:str=firstName
        self.lastName:str=lastName
        self.joinDate:datetime=joinDate
        self.friends=[]
        self.posts=[]