def top_one(parm):
    parm.sort()
    return parm[0]

print(top_one([4,2,3]))

def top_two(parm):
    parm.sort()
    return parm[:2]

parm = top_two([4,2,3])

print("top_tow is ", parm)