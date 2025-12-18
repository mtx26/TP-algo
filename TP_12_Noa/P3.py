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
        pass

    def ajouter_les_amis_d_amis(self):

        pass
        
    
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