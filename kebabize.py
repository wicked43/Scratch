def kebabize(string):
    new = ""
    for i in string:
        if string[0].isupper():
            i = i.lower()
        elif i.isupper():
            i = "-"+i.lower()
        elif not i.isalpha():
            continue
        new += i
    return new
print(kebabize("CodeWars"))
