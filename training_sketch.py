# def isValidWalk(walk):
#     return walk.count('n')==walk.count('s') and walk.count("w") == walk.count("e") and len(walk) == 10

# def is_isogram(string):
#     for i in string:
#         if string.lower().count(i) > 1:
#             return False
#     return True
#
# print(is_isogram("DermatoglySphics"))

# def tower_builder(n_floors):
#     return [("*"*(i*2-1)).center(n_floors*2-1) for i in range(1, n_floors+1)]
# print(tower_builder(10))

#def series_sum(n):
    #return "{:.2f}".format(sum(1.0/(1+3*i) for i in range(n)))
    # res = 1
    # for i in range(1, n):
    #     res += 1/(1+(3*i))
    # return "%.2f"% res
#print(series_sum(2))

def diamond(n):
    if n%2 != 0 and n > 0:
        star = "*"
        space = " "
        dia = []
        for i in range(1,n):
            dia.append(space*((n/2)-1) + star*(i*2-1)) + space*((n/2)-2) + "/n"
        return dia
print(diamond(3))
