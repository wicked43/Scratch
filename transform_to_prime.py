def minimum_number(numbers):
    num = sum(numbers)
    count = 0

    def check(numb, counter):
        for i in range(3, int(numb**0.5) + 1, 2):
            if numb%i == 0 or numb%2 == 0:
                numb += 1
                counter += 1
                check(numb, counter)
        return counter

    return check(num, count)

# def minimum_number(numbers):
#     num = sum(numbers)
#     while not check(num):
#         num += 1
#     return num - sum(numbers)
#
# def check(numb):
#     for i in range(3, int(numb**0.5) + 1, 2):
#         if numb%i == 0 or numb%2 == 0:
#             return False
#     return True

print(minimum_number([2,12,8,4,6]))

