def create_phone_number(n):
    new = "".join(str(e) for e in n)
    return "(%s)"%new[0:3] + " " + "%s"%new[3:6] + "-" + "%s"%new[6:10]
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))