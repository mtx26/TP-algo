class Drink :
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    def __str__(self):
        return str(self.name)
    
class Cocktail :
    def __init__(self, name, contents, quantities):
        self.name = name
        self.contents = contents
        self.quantities = quantities
    
    def __str__(self):
        return str(self.name)
    
    def est_alcoolisee(c):
        for i in c.contents :
            if i.volume != 0 :
                return True
        return False
    
    def cocktail_contenant(lc, b):
        liste = []
        for c in lc :
            for drinks in c.contents :
                if str(drinks) == b :
                    liste.append(c)
        return liste
    
    def taux_alcool(c):
        taux = 0
        for i in c.contents :
            taux = taux + c.quantities[i]*i.volume
        return taux



    


    