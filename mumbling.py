def accum(s):
    s = s.lower()
    new_s = []
    cur = 1
    for i in s:
        new_s.append(i.upper() + (i*(cur-1)))
        cur +=1
    return ("-".join(new_s))

print(accum("abcd"))


