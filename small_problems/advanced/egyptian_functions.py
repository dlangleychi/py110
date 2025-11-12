'''
P: egyptian: given fraction, return list on of denoms of
    unit fractions that sum to input
    unegyptian: given list of unit fraction denominators,
    return fraction of object of the sum of unit fractions
E: egyptian: Fraction(2, 1) -> [1, 2, 3, 6]
    unegyptian: [1, 2, 3, 6] -> Fraction(2, 1)
D: none
A: egyptian while numerator isn't one subtract any unit fraction
    which is less than value, record denom
    unegyptian: add unit fractions
C: below
'''

from fractions import Fraction

def egyptian(frac):
    result = []
    denom = 1
    while frac.numerator != 1:
        if frac >= Fraction(1, denom):
            frac -= Fraction(1, denom)
            result.append(denom)
        denom += 1
    result.append(frac.denominator)
    return result

def unegyptian(denom_list):
    result = Fraction(0,1)
    for denom in denom_list:
        result += Fraction(1, denom)
    return result

from fractions import Fraction

# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))