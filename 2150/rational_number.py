class RationalNumber:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def to_decimal(self):
        return float(self.numerator / self.denominator)

    def __eq__(self, other):
        return -.001 < self.to_decimal() - other.to_decimal() < .001

    def __lt__(self, other):
        return self.to_decimal() < other.to_decimal()

    def add(self, other):
        self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator

    def multiply(self, other):
        if isinstance(other, RationalNumber):
            self.numerator *= other.numerator
            self.denominator *= other.denominator

r1 = RationalNumber(2, 4)
r2 = RationalNumber(1, 2)
r3 = RationalNumber(1, 3)

print(r1) # should show 2/4
print(r2) # should show 1/2
print(r3) # should show 1/3

print(r1.to_decimal()) # should show 0.5
print(r2.to_decimal()) # should show 0.5

print(r1 == r2) # should show True
print(r1 == r3) # should show False
print(r1 < r2) # should show False
print(r3 < r1) # should show True

r1.add(r2)
print(r1) # should show 8/8

r2.multiply(r3)
print(r2) # should show 1/6um.to_decimal())