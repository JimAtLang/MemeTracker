from dataclasses import *
from dataToUsers import dataToUsers
from ReadFile import readfile
from stuff import import_friends

lines = readfile()
users = dataToUsers(lines)
import_friends(lines, users)