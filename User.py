import datetime

class User:
    def __init__(self, posts, firstName:str="", lastName:str="", friends=""):
        self.firstName:str=firstName
        self.lastName:str=lastName
        self.friends=[]
        self.posts=[]