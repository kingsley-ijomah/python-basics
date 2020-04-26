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
        numer = self.numer * other.denom + self.denom * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __sub__(self, other):
        numer = self.numer * other.denom - self.denom * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = self.denom * other.numer
        return Rational(numer, denom)

    def __abs__(self):
        numer = abs(self.numer)
        denom = abs(self.denom)
        return Rational(numer, denom)

    def __pow__(self, power):
        numer = pow(self.numer, power)
        denom = pow(self.denom, power)
        return Rational(numer, denom)

    def __rpow__(self, base):
        pass
