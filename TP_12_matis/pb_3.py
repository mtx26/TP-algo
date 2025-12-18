
class Personne:
    def __init__(self, nom, email, amis):
        if not isinstance(nom, str):
            raise ValueError("Le nom doit etre un sting")
        if not isinstance(email, str):
            raise ValueError("L'email doit etre un sting")
        if not isinstance(amis, list):
            raise ValueError("Le nom doit etre un sting")
        self.nom = nom
        self.email = email
        self.amis = amis
        
        
    def ajouter_un_ami(self, ami):
        if not isinstance(ami, Personne):
            raise ValueError
        if ami == self:
            raise ImportError
        if ami in self.amis:
            raise AssertionError
        else:
            self.amis.append(ami)
            
    def ajouter_les_amis_d_amis(self):
        for ami in self.amis:
            for a in ami.amis:
                try:
                    self.ajouter_un_ami(a)
                except:
                    pass
        

class Reseau:
    def __init__(self, personnes):
        if not isinstance(personnes, list):
            raise ValueError
        for personne in personnes:
            if not isinstance(personne, Personne):
                raise ValueError
        self.personnes = personnes
        
    def non_narcissique(self):
        for personne in self.personnes:
            if personne in personne.amis:
                return False
        return True
            
alice = Personne("Alice", "alice@email.com", [])
alice.amis.append(alice)
jean = Personne("jean", "jean", [])
bob = Personne("Bob", "bob@email.com", [jean])
alice.ajouter_un_ami(bob)  # Alice et Bob sont amis
alice.ajouter_les_amis_d_amis()
# Création du réseau
reseau = Reseau([alice, bob])

# Vérification si le réseau est non narcissique
print(reseau.non_narcissique()) 