class Rational:
    """
    Rational class for handling fractional numbers.
    Supports arithmetic operations, simplification, and conversion from int, float, and str.
    """

    def __init__(self, num=0, den=1):
        """Create a Rational from integers, floats or strings.

        Accepts `num`/`den` as integers, a single float (as `num`), or a
        string like '3/4', '0.25' or '3'. Performs type validation,
        simplification and normalises the sign so the denominator is
        always positive.
        """
        if isinstance(num, bool):
             raise ValueError(f"Cannot create a rational with a numerator of {str(type(num))}")
        if isinstance(den, bool):
             raise ValueError(f"Cannot create a rational with a denominator of {str(type(den))}")
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
        elif isinstance(num, str):
            if den != 1:
                 raise ValueError(f"Cannot create a rational with a denominator of {str(type(den))}")
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
                 raise ValueError(f"Cannot create a rational with a numerator of {str(type(num))}")
        # Validate types (must be int after conversion logic)
        if not isinstance(num, int):
            raise ValueError(f"Cannot create a rational with a numerator of {str(type(num))}")
        if not isinstance(den, int):
            raise ValueError(f"Cannot create a rational with a denominator of {str(type(den))}")
        if den == 0:
            raise ZeroDivisionError("Cannot create 3/0: zero in denominator")
        common = self._gcd(abs(num), abs(den))
        self._num = abs(num) // common
        self._den = abs(den) // common
        if (num < 0 and den > 0) or (num > 0 and den < 0):
            self._num = -self._num

    def _gcd(self, a, b):
        """Helper method to calculate Greatest Common Divisor"""
        while b:
            a, b = b, a % b
        return a
    def get_numerator(self):
        """Return the numerator of the rational (may be negative)."""
        return self._num

    def get_denominator(self):
        """Return the (always positive) denominator of the rational."""
        return self._den
    def __str__(self):
        """Return a human-friendly string: 'num/den' or 'num' if denominator is 1."""
        if self._den == 1:
            return str(self._num)
        return f"{self._num}/{self._den}"

    def __repr__(self):
        """Return the formal representation `Rational(num, den)`."""
        return f"Rational({self._num}, {self._den})"

    def __float__(self):
        """Return the approximate float value of the rational."""
        return self._num / self._den

    def __add__(self, other):
        """Add another Rational (or convertible value) and return a new Rational."""
        if not isinstance(other, Rational):
            try:
                other = Rational(other)
            except Exception:
                return NotImplemented

        new_num = self._num * other._den + other._num * self._den
        new_den = self._den * other._den
        return Rational(new_num, new_den)

    def __radd__(self, other):
        """Right-hand addition support: other + self."""
        return self + other

    def __mul__(self, other):
        """Multiply by another Rational (or convertible value)."""
        if not isinstance(other, Rational):
            try:
                other = Rational(other)
            except Exception:
                return NotImplemented

        return Rational(self._num * other._num, self._den * other._den)

    def __rmul__(self, other):
        """Right-hand multiplication support: other * self."""
        return self * other