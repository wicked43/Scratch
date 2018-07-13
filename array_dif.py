def array_diff(a, b):
    fn = []
    for x in a:
        if x not in b:
            fn.append(x)
    return fn
print(array_diff([1,2], [1]))