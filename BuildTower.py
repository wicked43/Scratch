def tower_builder(n_floors):
    out = []
    for i in range(1,n_floors+1):
        out.append(" "*(n_floors-i) + "*"*(2*i-1) + " "*(n_floors-i))
    return out
print(tower_builder(8))


#best solution

#def tower_builder(n):
    #return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]