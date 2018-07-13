def is_isogram(string):
    new = ""
    for i in string:
        if i in new:
            return False
        else:
            new += i
    return True

print(is_isogram("fap"))