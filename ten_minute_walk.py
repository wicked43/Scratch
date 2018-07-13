# def isValidWalk(walk):
#     x = 0
#     y = 0
#     for i in walk:
#         i = str(i)
#         if i == "n":
#             y +=1
#         elif i == "s":
#             y -=1
#         elif i == "e":
#             x +=1
#         elif i == "w":
#             x -=1
#     if x == 0 and y == 0 and len(walk) == 10:
#         return True
#     elif x+y == (11-len(walk)):
#         return True
#     else:
#         return False

def isValidWalk(walk):
    if len(walk)== 10 and walk.count("n") - walk.count("s") == 0 and walk.count("e") - walk.count("w") == 0:
        return True
    return False

