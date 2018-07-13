def find_it(seq):
    for j in seq:
        if seq.count(j)%2!=0:
            return j
print(find_it([10,10,9,9,9]))

