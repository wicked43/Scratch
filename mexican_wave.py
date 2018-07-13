def wave(str):
    str = str.lower()
    new = []
    for i in range(len(str)):
        if str[i].isalpha():
            new.append(str[:i]+str[i].upper()+str[i+1:])
    return new

print(wave("fapfapfap"))
