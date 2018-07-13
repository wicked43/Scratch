def get_middle(s):
    x = int(len(s) / 2)
    if len(s)%2 == 0:
        print(x)
        return s[x-1]+s[x]
    else:
        return s[x//2]


#better solution
#def get_middle(s):
    #i = (len(s) - 1) // 2
    #return s[i:-i] or s


print(get_middle("testee"))