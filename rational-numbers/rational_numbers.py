from __future__ import division
from math import gcd


class Rational:
    def __init__(self, numer, denom):
        self.numer, self.denom  = Rational.reduce(numer, denom)
        self.numer = -self.numer if self.denom < 0 else self.numer

    @classmethod
    def reduce(cls, numer, denom):
        _gcd = gcd(numer, denom)
        return (numer // _gcd, denom // _gcd)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __abs__(self):
        pass

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass
