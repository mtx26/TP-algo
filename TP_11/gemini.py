class Rational:
    """
    Rational class for handling fractional numbers.
    Supports arithmetic operations, simplification, and conversion from int, float, and str.
    """

    def __init__(self, num=0, den=1):
        # Handle Boolean inputs first (bool is a subclass of int in Python)
        if isinstance(num, bool):
             raise ValueError(f"Cannot create a rational with a numerator of {str(type(num))}")
        if isinstance(den, bool):
             raise ValueError(f"Cannot create a rational with a denominator of {str(type(den))}")

        # Handle Float inputs (Single argument)
        if isinstance(num, float):
            if den != 1:
                raise ValueError(f"Cannot create a rational with a denominator of {str(type(den))}")
            s = str(num)
            if '.' in s:
                int_part, dec_part = s.split('.')
                # Convert 1.234 to 1234 / 1000
                num = int(int_part + dec_part)
                den = 10 ** len(dec_part)
            else:
                num = int(num)
                den = 1

        # Handle String inputs (Required for pyRat calculator)
        elif isinstance(num, str):
            if den != 1:
                 raise ValueError(f"Cannot create a rational with a denominator of {str(type(den))}")
            
            # Logic to parse strings like "1/2", "0.25", or "3"
            try:
                if '/' in num:
                    parts = num.split('/')
                    if len(parts) != 2:
                         raise ValueError()
                    num = int(parts[0])
                    den = int(parts[1])
                elif '.' in num:
                     int_part, dec_part = num.split('.')
                     num = int(int_part + dec_part)
                     den = 10 ** len(dec_part)
                else:
                    num = int(num)
                    den = 1
            except ValueError:
                 # Maintain consistency with Type checks for invalid strings
                 raise ValueError(f"Cannot create a rational with a numerator of {str(type(num))}")

        # Validate types (must be int after conversion logic)
        if not isinstance(num, int):
            raise ValueError(f"Cannot create a rational with a numerator of {str(type(num))}")
        if not isinstance(den, int):
            raise ValueError(f"Cannot create a rational with a denominator of {str(type(den))}")

        # Check for division by zero
        if den == 0:
            raise ZeroDivisionError("Cannot create 3/0: zero in denominator")

        # Simplify automatically using GCD
        common = self._gcd(abs(num), abs(den))
        self._num = abs(num) // common
        self._den = abs(den) // common

        # Handle signs (Denominator should be positive)
        if (num < 0 and den > 0) or (num > 0 and den < 0):
            self._num = -self._num

    def _gcd(self, a, b):
        """Helper method to calculate Greatest Common Divisor"""
        while b:
            a, b = b, a % b
        return a

    # Accessors
    def get_numerator(self):
        return self._num

    def get_denominator(self):
        return self._den

    # String representation: "num/den" or "num" if den is 1
    def __str__(self):
        if self._den == 1:
            return str(self._num)
        return f"{self._num}/{self._den}"

    # Formal representation: Rational(num, den)
    def __repr__(self):
        return f"Rational({self._num}, {self._den})"

    # Float conversion
    def __float__(self):
        return self._num / self._den

    # Arithmetic Operations (Add/Mul)
    def __add__(self, other):
        if not isinstance(other, Rational):
            try:
                other = Rational(other)
            except Exception:
                return NotImplemented
        
        new_num = self._num * other._den + other._num * self._den
        new_den = self._den * other._den
        return Rational(new_num, new_den)

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if not isinstance(other, Rational):
            try:
                other = Rational(other)
            except Exception:
                return NotImplemented
        
        return Rational(self._num * other._num, self._den * other._den)

    def __rmul__(self, other):
        return self * other