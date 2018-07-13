def iq_test(numbers):
    evn = []
    odd = []
    lst = [int(x) for x in numbers.split(" ")]
    for i in lst:
        if i %2 ==0:
            evn.append(i)
        else:
            odd.append(i)
    if len(evn) == 1:
        return evn
    else:
        return odd

iq_test("2 4 7 8 10")
