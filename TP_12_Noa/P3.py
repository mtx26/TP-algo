class Personne():

    def __init__(self, name, email, friends):

        if not isinstance(name, str): 
            raise ValueError("Attention, le nom de la personne doit etre une chaine de caractère !")
        if not isinstance(email, str): 
            raise ValueError("Attention, l'email de la personne doit etre une chaine de caractère !")
        if not isinstance(friends, list): 
            raise ValueError("Attention, la liste d'amis de la personne doit etre une liste python !")
            

        self.name = name
        self.email = email
        self.friends = []

    def ajouter_un_ami(self, ami):
        if ami is not self and ami not in self.amis:
            self.amis.append(ami)
        return ami

    def ajouter_les_amis_d_amis(self):
        amis_a_ajouter = []
        for ami_direct in self.amis:
            for ami_dist in ami_direct.amis:
                if (ami_dist is not self) and \
                   (ami_dist not in self.amis) and \
                   (ami_dist not in amis_a_ajouter):
                    amis_a_ajouter.append(ami_dist)
        
        self.amis.extend(amis_a_ajouter)
    
    def __str__(self):
        return "Une personne, sont nom est " + self.name + "son adresse email est " + self.email + "ses amis sont " + self.friends


class Reseau(Personne):
    def __init__(self, liste):
        if not isinstance(liste, list): 
            raise ValueError("Attention, la liste d'amis de la personne doit etre une liste python !")
        
    def non_narcissique(self):
        pass

if __name__== "__main__":
    pass