import math

def get_pgcd(x, y):
    return math.gcd(x, y)

def simplified(n, d):
    pgcd = get_pgcd(d, n)
    n = n / pgcd
    d = d / pgcd
    return(int(n), int(d))

def float_to_str(x):
    i = 0
    while x % 1 != 0:
        x = x * 10
        i += 1
    return int(x), 10**i

def to_rational(self):
    if isinstance(self, int):
        self = Rational(self)
    elif isinstance(self, float):
        n, d = float_to_str(self)
        self = Rational(n, d)
    return self
    

def rational_add(self, other):
    n = self.n * other.d + self.d * other.n
    d = self.d * other.d

    n, d = simplified(n, d)

    return Rational(n, d)

def rational_mul(self, other):
    n = self.n * other.n
    d = self.d * other.d

    n, d = simplified(n, d)

    return Rational(n, d)

class Rational():

    def __init__(self, n, d=1):
        if d == 0:
            raise ZeroDivisionError
        self.n = n
        self.d = d

    def __str__(self):
        if self.d == 1:
            return str(self.n)
        s = '%g/%g' % (self.n, self.d)
        return s
    
    def __getitem__(self, index):
        if index == 0:
            return self.n
        elif index == 1:
            return self.d
        else:
            raise IndexError
    
    def __setitem__(self, index, value):
        if index == 0:
            self.update(value, self.d)
        elif index == 1:
            self.update(self.n, value)
        else:
            raise IndexError
    
    def update(self, n, d):
        self.n = n
        self.d = d
    
    def __add__(self, other):
        self = to_rational(self)
        other = to_rational(other)
        return rational_add(self, other)
    
    def __radd__(self, other):
        return to_rational(other).__add__(self)
    
    def __sub__(self, other):
        self = to_rational(self)
        other = to_rational(other)
        return rational_add(self, Rational(-other.n, other.d))

    def __rsub__(self, other):
        return to_rational(other).__sub__(self)
    
    def __mul__(self, other):
        self = to_rational(self)
        other = to_rational(other)
        return rational_mul(self, other)
    
    def __rmul__(self, other):
        return to_rational(other).__mul__(self)

    def  __truediv__(self, other):
        self = to_rational(self)
        other = to_rational(other)
        other.update(other.d, other.n)
        return rational_mul(self, other)
    
    def  __rtruediv__(self, other):
        return to_rational(other).__truediv__(self)
    

if __name__== "__main__":
    p = Rational(5, 2)
    q = Rational(2, 56)
    j = Rational(2)
    j[0] = 45
    a = 2 / q