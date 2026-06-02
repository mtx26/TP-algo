import math


class Rational():
    def __init__(self, x=0, y=1):
        if type(x) != int :
            if type(x) == float and y == 1 :
                x = str(x)
                new_x = ''
                cnt = 0
                for i in range(len(x)):
                    if x[i] != '.':
                        new_x = new_x + x[i]
                        cnt = cnt + 1
                x = int(new_x)
                y = 10**(cnt-1)
            elif type(x) == str :
                for i in range(len(x)):
                    if not x[i].isdigit() and x[i] != '/' and x[i] != ' '  and x[i] != '.':
                        raise ValueError('Cannot create a rational from this str: '+ x )
                if '/' in x :
                    x_new = ''
                    y_new = ''
                    i = 0
                    while x[i] != '/' :
                        if x[i].isdigit():
                            x_new = x_new + x[i]
                        i = i + 1
                    while i < len(x):
                        if x[i].isdigit():
                            y_new = y_new + x[i]
                        i = i + 1
                    x = int(x_new)
                    y = int(y_new)

                elif '.' in x :
                    new_x = ''
                    cnt = 0
                    for i in range(len(x)):
                        if x[i] != '.' and x[i] != ' ':
                            new_x = new_x + x[i]
                            cnt = cnt + 1
                    x = int(new_x)
                    y = 10**(cnt-1)
                
                else :
                    new_x = ''
                    for i in range(len(x)):
                        if x[i] != ' ':
                            new_x = new_x + x[i]
                    x = int(new_x)
            else :
                raise ValueError('Cannot create a rational with a numerator of '+ str(type(x)))
        if type(y) != int :
            raise ValueError('Cannot create a rational with a denominator of '+ str(type(y)))
        if y == 0 :
            raise ZeroDivisionError('Cannot have zero as denominator')
        if y < 0 :
            x = -x
            y = -y
        self.x = x//math.gcd(x,y)
        self.y = y//math.gcd(x,y)

    def __str__(self):
        if self.y == 1 :
            frac = '%d' % (self.x)
        else :
            frac = '%d/%d' % (self.x , self.y)
        return frac
    def get_denominator(self):
        return self.y
    
    def __repr__(self):
        x = str(self.x)
        y = str(self.y)
        return "Rational("+ x +", "+ y +")"
    
    def __add__(self, other):
        if isinstance(other, Rational):
            new_x = (self.x * other.y) + (other.x * self.y)
            new_y = math.lcm(self.y, other.y)
            res = Rational(new_x, new_y)
            return res
        elif isinstance(other, int):
            p = Rational(other)
            new_x = (self.x * p.y) + (p.x * self.y)
            new_y = math.lcm(p.y, self.y)
            res = Rational(new_x, new_y)
            return res
        elif isinstance(other, float):
            q = Rational(other)
            new_x = (self.x * q.y) + (q.x * self.y)
            new_y = math.lcm(q.y, self.y)
            res = Rational(new_x, new_y)
            return res
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __mul__(self, other):
        if isinstance(other, Rational):
            new_x = self.x * other.x
            new_y = self.y * other.y
            res = Rational(new_x, new_y)
            return res
        elif isinstance(other, int):
            p = Rational(other)
            new_x = self.x * p.x
            new_y = self.y * p.y
            res = Rational(new_x, new_y)
            return res
        elif isinstance(other, float):
            q = Rational(other)
            new_x = self.x * q.x
            new_y = self.y * q.y
            res = Rational(new_x, new_y)
            return res
        
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __float__(self):
        f = self.x / self.y
        return f
    