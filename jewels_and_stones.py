def numJewelsInStones(J, S):
    counter = 0
    for i in J:
        if i in S:
            counter +=1
    return counter