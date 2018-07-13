def unique_in_order(iterable):
    lst = []
    if len(iterable)==0:
        return lst
    else:
        lst.append(iterable[0])
        for i in range(0,len(iterable)-1):
            if iterable[i] != iterable[i+1] and i < len(iterable):
                lst.append(iterable[i+1])
            print(iterable[i])
    return lst
print(unique_in_order('AAAABBBCCDAABBB'))

# def unique_in_order(iterable):
#     res = []
#     for item in iterable:
#         if len(res) == 0 or item != res[-1]:
#             res.append(item)
#     return res