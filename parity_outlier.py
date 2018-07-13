def find_outlier(integers):
    even = 0
    odd = 0
    if even <= 1 and odd <= 1:
        for i in integers:
            if %2 == 0:
                even += 1
            else:
                odd += 1
    if odd > 1:
        for i in integers:
            if i%2 == 0:
                return i
    if even > 1:
        for i in integers:
            if i%2 != 0:
                return i


