def tribonacci(signature,n):
    new = signature
    for i in range(n-3):
        x = signature[i+1]+signature[i]+signature[i+2]
        new.append(x)
    return new[:n]
print(Xbonacci([1,1,1], 10))
