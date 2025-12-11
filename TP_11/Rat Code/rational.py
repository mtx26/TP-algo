import math

def get_pgcd(n, d):
    return math.gcd(int(n), int(d))
    

def simplified(n, d):
    pgcd = get_pgcd(n, d)
    n = n / pgcd
    d = d / pgcd
    return (int(n), int(d))

def valide_caracter(x, special=None):
    """
    Vérifie que tous les caractères de x sont des chiffres ou dans les clés de special.
    Si special est un dict, limite le nombre d'occurrences de chaque caractère spécial indépendamment.
    Exemple : special={'.':1, '/':1, '-':2} limite à 1 point, 1 slash, 2 tirets.
    """
    if special is None:
        special = {}
    for k, v in special.items():
        if x.count(k) > v:
            return False
    return all(c.isdigit() or c in special for c in x)

def float_to_str(n, d):
    # Convertit deux floats en entiers pour une fraction exacte
    n_str = str(n)
    d_str = str(d)
    n_dec = n_str[::-1].find('.') if '.' in n_str else 0
    d_dec = d_str[::-1].find('.') if '.' in d_str else 0
    scale = 10 ** max(n_dec, d_dec)
    n_int = int(round(n * scale))
    d_int = int(round(d * scale))
    return n_int, d_int

class Rational():

    def __init__(self, n=0, d=1):

        if isinstance(n, Rational):
            n, d = n.n, n.d

        if isinstance(n, str):
            n = n.replace(' ', '')

            if not valide_caracter(n, special={'.':2, '/':1, '-':2}):
                raise ValueError(f"Cannot create a rational from this str: {n}")
            
            if '/' in n:
                num, den = n.split('/')
                if not valide_caracter(num, special={'.':1, '-':1}) or not valide_caracter(den, special={'.':1, '-':1}):
                    raise ValueError(f"Cannot create a rational from this str: {n}")
                
                n = float(num) if '.' in num else int(num)
                d = float(den) if '.' in den else int(den)
            else:
                if not valide_caracter(n, special={'.':1, '-':1}):
                    raise ValueError(f"Cannot create a rational from this str: {n}")
                
                n = float(n) if '.' in n else int(n)

        if isinstance(d, str):
            d = d.replace(' ', '')
            if not valide_caracter(den, special={'.':1, '-':1}):
                raise ValueError(f"Cannot create a rational from this str: {d}")
            
            d = float(d) if '.' in d else int(d)

        if isinstance(n, float) or isinstance(d, float):
            n, d = float_to_str(n, d)

        if isinstance(n, (list, bool)):
            raise ValueError(f"Cannot create a rational with a numerator of <class '{type(n)}'>")
        
        if isinstance(d, (list, bool)):
            raise ValueError(f"Cannot create a rational with a denominator of <class '{type(d)}'>")
 
        if d == 0:
            raise ZeroDivisionError(f"Cannot create {n}/{d}: zero in denominator")
        
        elif d < 0:
            n *= -1
            d *= -1
            
        n, d = simplified(n, d)
        self.n = n
        self.d = d

    def __str__(self):
        if self.d == 1:
            return str(self.n)
        return f"{self.n}/{self.d}"
    
    def __getitem__(self, index):
        if index == 0:
            return self.n
        elif index == 1:
            return self.d
        else:
            raise IndexError(f"Bad index for [] operator: use {index} but only 0 and 1 are accepted")

    def __setitem__(self, index, value):
        if index == 0:
            self.__init__(value, self.d)
        elif index == 1:
            self.__init__(self.n, value)
        else:
            raise IndexError(f"Bad index for [] operator: use {index} but only 0 and 1 are accepted")
    
    def get_numerator(self):
        return self.n
        
    def get_denominator(self):
        return self.d
    
    def __repr__(self):
        return f'Rational({self.n}, {self.d})'
    
    def __float__(self):
        return self.n / self.d
    
    def __add__(self, other):
        other = Rational(other)
        return Rational(self.n * other.d + self.d * other.n, self.d * other.d)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        other = Rational(other)
        return Rational(self.n * other.d - self.d * other.n, self.d * other.d)

    def __rsub__(self, other):
        return Rational(other).__sub__(self)

    def __mul__(self, other):
        other = Rational(other)
        return Rational(self.n * other.n, self.d * other.d)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        other = Rational(other)
        if other.n == 0:
            raise ZeroDivisionError("division by zero")
        return Rational(self.n * other.d, self.d * other.n)

    def __rtruediv__(self, other):
        return Rational(other).__truediv__(self)
    
    def __eq__(self, other):
        other = Rational(other)
        return self.n * other.d == self.d * other.n

    def __lt__(self, other):
        other = Rational(other)
        return self.n * other.d < self.d * other.n

    def __le__(self, other):
        other = Rational(other)
        return self.n * other.d <= self.d * other.n
    

if __name__== "__main__":
    p = Rational(5.3, 2.76)
    q = Rational(2, -56)
    
    print(p / 0)