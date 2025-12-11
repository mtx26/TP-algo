import math

def get_pgcd(n, d):
    return math.gcd(n, d)

def simplified(n, d):
    pgcd = get_pgcd(n, d)
    n = n / pgcd
    d = d / pgcd
    return(int(n), int(d))

def float_to_str(n, d):
    i = 0
    while n % 1 != 0:
        n = n * 10
        i += 1
    n = int(n)
    d = d * (10**i)
    j = 0
    while d % 1 != 0:
        d = d * 10
        j += 1
    d = int(d)
    n = n * (10**j)
    return n, d
    

def rational_add(self, other):
    n = self.n * other.d + self.d * other.n
    d = self.d * other.d
    return Rational(n, d)

def rational_mul(self, other):
    n = self.n * other.n
    d = self.d * other.d
    return Rational(n, d)

class Rational():

    def __init__(self, n=0, d=1):
        if isinstance(n, Rational):
            n, d = n.n, n.d
        if isinstance(n, str):
            n = n.replace(' ', '')
            if all(c.isdigit() or c == "/" or c == "." for c in n):
                if '/' in n:
                    num, den = n.split('/')
                    n = int(num)
                    d = int(den)
                else:
                    n = float(n)
            else:
                raise ValueError("Cannot create a rational from this str: %s" % n)
        
        if isinstance(d, str):
            d = d.replace(' ', '')
            if all(c.isdigit() for c in d):
                d = float(n)
            else:
                raise ValueError("Cannot create a rational from this str: %s" % d) 

        if isinstance(n, float) or isinstance(d, float):
            n, d = float_to_str(n, d)

        if isinstance(n, (list, bool)):
            raise ValueError("Cannot create a rational with a numerator of <class '%s'>" % type(n))
        
        if isinstance(d, (list, bool)):
            raise ValueError("Cannot create a rational with a denominator of <class '%s'>" % type(d))


        if d == 0:
            raise ZeroDivisionError("Cannot create %g/%g: zero in denominator" % (n, d))
        elif d < 0:
            n *= -1
            d *= -1

        n, d = simplified(n, d)

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
            raise IndexError("Bad index for [] operator: use %g but only 0 and 1 are accepted" % index)
    
    def __setitem__(self, index, value):
        if index == 0:
            self.n = value
            self.__init__(self.n, self.d)
        elif index == 1:
            self.d = value
            self.__init__(self.n, self.d)
        else:
            raise IndexError("Bad index for [] operator: use %g but only 0 and 1 are accepted" % index)
    
    def get_numerator(self):
        return self.n
        
    def get_denominator(self):
        return self.d
    
    def __repr__(self):
        return f'Rational({self.n}, {self.d})'
    
    def __float__(self):
        return self.n / self.d
    
    def __add__(self, other):
        return rational_add(Rational(self), Rational(other))
    
    def __radd__(self, other):
        return Rational(other).__add__(self)
    
    def __sub__(self, other):
        self = Rational(self)
        other = Rational(other)
        return rational_add(self, Rational(-other.n, other.d))

    def __rsub__(self, other):
        return Rational(other).__sub__(self)
    
    def __mul__(self, other):
        self = Rational(self)
        other = Rational(other)
        return rational_mul(self, other)
    
    def __rmul__(self, other):
        return Rational(other).__mul__(self)

    def  __truediv__(self, other):
        self = Rational(self)
        other = Rational(other)
        return rational_mul(self, Rational(other.d, other.n))
    
    def  __rtruediv__(self, other):
        return Rational(other).__truediv__(self)
    
    def __eq__(self, other):
        self = Rational(self)
        other = Rational(other)
        return self.n * other.d == self.d * other.n
    
    def __lt__(self, other):
        self = Rational(self)
        other = Rational(other) 
        return self.n * other.d < self.d * other.n
    
    def __le__(self, other):
        self = Rational(self)
        other = Rational(other) 
        return self.n * other.d <= self.d * other.n
    

if __name__== "__main__":
    p = Rational(5.3, 2.76)
    q = Rational(2, -56)
    
    print(p)