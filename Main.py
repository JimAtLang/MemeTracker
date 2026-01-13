from FriendTracker import get_friends

fd = get_friends()
print(fd)
for _ in fd:
    print(f"{_}has {len(fd[_])} friends!")