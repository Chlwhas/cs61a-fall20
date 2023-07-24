def add_complex_to_rational(c, r):
    return ComplexRI(c.real + r.numer / r.denom, c.imag)


def add_rational_to_complex(r, c):
    return add_complex_to_rational(c, r)


def mul_complex_to_rational(c, r):
    r.magnitude, r.angle = r.numer / r.denom, 0
    if r.magnitude < 0:
        r.magnitude = -r.magnitude
        r.angle = pi
    return ComplexMA(c.magnitude * r.magnitude, c.angle + r.angle)


def mul_rational_to_complex(r, c):
    return mul_complex_to_rational(c, r)


class Number:
    def __add__(self, other):
        if self.type_tag == other.type_tag:
            return self.add(other)
        elif (self.type_tag, other.type_tag) in self.adders:
            return self.cross_apply(other, self.adders)

    def __mul__(self, other):
        if self.type_tag == other.type_tag:
            return self.mul(other)
        elif (self.type_tag, other.type_tag) in self.multipliers:
            return self.cross_apply(other, self.multipliers)

    def cross_apply(self, other, cross_fns):
        cross_fn = cross_fns[(self.type_tag, other.type_tag)]
        return cross_fn(self, other)

    adders = {
        ("com", "rat"): add_complex_to_rational,
        ("rat", "com"): add_rational_to_complex
    }

    multipliers = {
        ("com", "rat"): mul_complex_to_rational,
        ("rat", "com"): mul_rational_to_complex
    }


from math import pi


class Complex(Number):
    type_tag = "com"

    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)

    def mul(self, other):
        return ComplexMA(self.magnitude * other.magnitude, self.angle + other.angle)


from math import atan2


class ComplexRI(Complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):
        return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.imag)

    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    @property
    def angle(self):
        return atan2(self.imag, self.real)


from math import sin, cos


class ComplexMA(Complex):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    def __repr__(self):
        return 'ComplexMA({0:g}, {1:g} * pi)'.format(self.magnitude, self.angle / pi)

    @property
    def real(self):
        return cos(self.angle) * self.magnitude

    @property
    def imag(self):
        return sin(self.angle) * self.magnitude


from math import gcd


class Rational(Number):
    type_tag = "rat"

    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g

    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.numer, self.denom)

    def add(self, other):
        nx, dx = self.numer, self.denom
        ny, dy = other.numer, other.denom
        return Rational(nx * dy + dx * ny, dx * dy)

    def mul(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)


