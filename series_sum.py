def series_sum(n):
    x = 1
    f = 4
    for i in range(1, n+1):
        x = x + (1/f)
        f += 3
    return '%.2f' % x

print(series_sum(12))