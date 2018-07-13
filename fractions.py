def reduc(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n

class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        common = reduc(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other):
        first_n = self.num * other.den
        sec_n = self.den * other.num
        return first_n == sec_n

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = reduc(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        common = reduc(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den = other.den
        return 




print(Fraction(1,2) / Fraction(1,2))