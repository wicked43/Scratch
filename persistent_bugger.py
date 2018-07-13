def persistence(n):
    count = 0
    def persistence2(n, count):
        n = list(str(n))
        new = []
        if len(n) > 1:
            a = int(n[0])
            for i in range(1, len(n)):
                a *= int(n[i])
            new.append(int(a))
            new = "".join(map(str, new))
            count += 1
            return persistence2(int(new), count)
        return count
    return persistence2(n, count)

print(persistence(123))
