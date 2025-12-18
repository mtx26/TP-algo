import math

def get_pgcd(n, d):
    """Retourne le plus grand commun diviseur (PGCD) de deux valeurs.

    Args:
        n (int|float|str): Première valeur; sera convertie en int avant calcul.
        d (int|float|str): Deuxième valeur; sera convertie en int avant calcul.

    Returns:
        int: PGCD de int(n) et int(d).
    """
    return math.gcd(int(n), int(d))
    

def simplified(n, d):
    """Simplifie une fraction en divisant numérateur et dénominateur par leur PGCD.

    Args:
        n (int|float): Numérateur.
        d (int|float): Dénominateur.

    Returns:
        tuple[int, int]: Numérateur et dénominateur simplifiés sous forme d'entiers (n, d).
    """
    pgcd = get_pgcd(n, d)
    n = n / pgcd
    d = d / pgcd
    return (int(n), int(d))

def valide_caracter(x, special=None):
    """Vérifie si une chaîne contient uniquement des chiffres et des caractères autorisés.

    Args:
        x (str): Chaîne à vérifier.
        special (dict, optional): Dictionnaire où chaque clé est un caractère spécial autorisé
            et la valeur est le nombre maximal d'occurrences autorisées pour ce caractère.
            Si None, aucun caractère spécial n'est autorisé.

    Returns:
        bool: True si la chaîne est valide selon les règles, False sinon.

    Exemple:
        special={'.':1, '/':1, '-':2} autorise au plus 1 point, 1 slash et 2 tirets.
    """
    if special is None:
        special = {}
    for k, v in special.items():
        if x.count(k) > v:
            return False
    return all(c.isdigit() or c in special for c in x)

def float_to_str(n, d):
    """Convertit deux réels en entiers proportionnels pour représenter une fraction exacte.

    Cette fonction calcule une échelle basée sur le nombre de décimales et renvoie
    (n_int, d_int) tels que n/d == n_int/d_int si possible.

    Args:
        n (int|float): Numérateur.
        d (int|float): Dénominateur.

    Returns:
        tuple[int, int]: Numérateur et dénominateur convertis en entiers proportionnels.
    """
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
        """Initialise un objet Rational et normalise la fraction.

        Le constructeur accepte plusieurs formats pour `n` et `d` :
        - entiers (int), flottants (float), chaînes (str) du type 'a/b' ou 'x.y',
        - un autre objet Rational (copie).

        Args:
            n (int|float|str|Rational): Numérateur ou représentation de la fraction.
            d (int|float|str): Dénominateur (optionnel si `n` est une chaîne contenant '/').

        Raises:
            ValueError: si la chaîne fournie a un format invalide ou si des types non supportés
                        (list, bool) sont passés pour n ou d.
            ZeroDivisionError: si le dénominateur (après conversion) vaut 0.
        """

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
        """Représentation lisible de la fraction.

        Returns:
            str: "n" si le dénominateur vaut 1, sinon "n/d".
        """
        if self.d == 1:
            return str(self.n)
        return f"{self.n}/{self.d}"
    
    def __getitem__(self, index):
        """Accès par index : 0 -> numérateur, 1 -> dénominateur.

        Args:
            index (int): 0 pour le numérateur, 1 pour le dénominateur.

        Returns:
            int: Numérateur ou dénominateur selon l'index.

        Raises:
            IndexError: si l'index n'est pas 0 ou 1.
        """
        if index == 0:
            return self.n

        elif index == 1:
            return self.d
        else:
            raise IndexError(f"Bad index for [] operator: use {index} but only 0 and 1 are accepted")

    def __setitem__(self, index, value):
        """Modifie le numérateur ou le dénominateur via l'opérateur []=.

        Args:
            index (int): 0 pour modifier le numérateur, 1 pour modifier le dénominateur.
            value (int|float|str|Rational): Nouvelle valeur pour la partie sélectionnée.

        Raises:
            IndexError: si l'index n'est pas 0 ou 1.
        """
        if index == 0:
            self.__init__(value, self.d)
        elif index == 1:
            self.__init__(self.n, value)
        else:
            raise IndexError(f"Bad index for [] operator: use {index} but only 0 and 1 are accepted")
    
    def get_numerator(self):
        """Retourne le numérateur de la fraction.

        Returns:
            int: Numérateur.
        """
        return self.n
        
    def get_denominator(self):
        """Retourne le dénominateur de la fraction.

        Returns:
            int: Dénominateur.
        """
        return self.d
    
    def __repr__(self):
        """Représentation officielle utilisable pour recréer l'objet.

        Returns:
            str: Chaîne du type "Rational(n, d)".
        """
        return f'Rational({self.n}, {self.d})'
    
    def __float__(self):
        """Convertit la fraction en flottant.

        Returns:
            float: Résultat de n / d.
        """
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
        """Division de deux rationnels.

        Args:
            other (int|float|str|Rational): Diviseur.

        Returns:
            Rational: Résultat de la division self / other.

        Raises:
            ZeroDivisionError: si `other` est équivalent à 0.
        """
        other = Rational(other)
        if other.n == 0:
            raise ZeroDivisionError("division by zero")
        return Rational(self.n * other.d, self.d * other.n)

    def __rtruediv__(self, other):
        return Rational(other).__truediv__(self)
    
    def __eq__(self, other):
        """Comparaison d'égalité entre rationnels.

        Args:
            other (int|float|str|Rational): Valeur à comparer.

        Returns:
            bool: True si les deux rationnels sont égaux.
        """
        other = Rational(other)
        return self.n * other.d == self.d * other.n

    def __lt__(self, other):
        """Comparaison stricte (<) entre rationnels.

        Args:
            other (int|float|str|Rational): Valeur à comparer.

        Returns:
            bool: True si self < other.
        """
        other = Rational(other)
        return self.n * other.d < self.d * other.n

    def __le__(self, other):
        """Comparaison inférieure ou égale (<=) entre rationnels.

        Args:
            other (int|float|str|Rational): Valeur à comparer.

        Returns:
            bool: True si self <= other.
        """
        other = Rational(other)
        return self.n * other.d <= self.d * other.n
    

if __name__== "__main__":
    p = Rational(5.3, 2.76)
    q = Rational(2, -56)
    
    print(p / 0)