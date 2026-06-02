class Personne :
    def __init__(self, nom = 'test', email = 'test@gmail.com', amis=None):
        self.nom = nom
        self.email = email
        self.amis = amis

    def ajouter_un_ami(self, ami):
        if ami not in self.amis and ami != self :
            self.amis.append(ami)
        
    def __str__(self):
        return str(self.nom)
    
    def ajouter_les_amis_d_amis(self):
        for a in self.amis :
            for f in a.amis :
                if f not in self.ami and f != self:
                    self.ajouter_un_ami(f)

class Reseau :
    def __init__(self, personnes):
        self.personnes = personnes

    def non_narcissique(self):
        for i in self.personnes :
            if i in i.amis :
                return False
        return True