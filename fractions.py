def reduc(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n


class Fraction:

    def __init__(self, top, bottom):
        if isinstance(top, int) and isinstance(bottom, int):
            pass
        else:
            raise ValueError("Values are no Integers!")

        self.num = top // reduc(top, bottom)
        self.den = bottom // reduc(top, bottom)

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __repr__(self):
        return f'{self.num}/{self.den}'

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        first_n = self.num * other.den
        sec_n = self.den * other.num
        return first_n == sec_n

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __lt__(self, other):
        first_n = self.num / self.den
        sec_n = other.num / other.den
        return first_n < sec_n

    def __ge__(self, other):
        first_n = self.num / self.den
        sec_n = other.num / other.den
        return first_n >= sec_n

    def __radd__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __iadd__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)


tst = Fraction(1, 2)
tst += Fraction(1, 3)
print(Fraction(1, 2) + Fraction(1, 3))
print(tst)
