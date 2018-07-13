def tickets(people):
    twfiv = 0
    fif = 0
    for i in people:
        if i == 25:
            twfiv += 1
        elif i != 25:
            if i == 50 and twfiv < 1:
                return False
            elif i == 50 and twfiv >= 1:
                twfiv -= 1
                fif +=1
            elif i == 100:
                if fif >= 1 and twfiv >=1:
                    fif -= 1
                    twfiv -= 1
                elif twfiv >= 3:
                    twfiv -=3
                else:
                    return False
        #print(twfiv)
        #print(fif)
        #print("--------------")
    return True


print(tickets([25, 25, 50, 50, 100]))
