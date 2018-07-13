def longest_consec(st, k):
    new = ""
    if k > 0 and len(st)>=0:
        for i in range(0, len(st)-k+1):
            new1 = ("".join(st[i:i+k]))
            if len(new1) > len(new):
                new = new1
    return new

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
#print(longest_consec([], 3))
#print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
#print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2))