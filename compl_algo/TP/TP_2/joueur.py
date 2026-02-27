import random

class Node:  
    def __init__(self, data = 0, next = None):
        self.data: Joueur = data
        self.next: Node = next
        
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return repr(self.data) + ' -> ' + repr(self.next)
    
    def set_next(self, next):
        self.next = next
        
    def get_next(self):
        return self.next
    
    def set_data(self, data):
        self.data = data
        
    def get_data(self):
        return self.data
   
class ListeChainee:
    def __init__(self):
        self.n = 0
        self.first = None
        self.last = None
        
    def __repr__(self):
        return repr(self.first)
    
    def insert_first(self, data):
        self.first = Node(data, self.first)
        if self.last is None:
            self.last = self.first
        self.n += 1
        
    def insert_last(self, data):
        if self.last is None:
            self.first = self.last = Node(data)
        else:
            self.last.next = Node(data)
            self.last = self.last.next
        self.n += 1    
        
    def get_first(self):
        if self.first is None:
            raise ValueError('Structure is empty')
        return self.first.data

    def remove_first(self):
        if self.first is None:
            raise ValueError('Structure is empty')
        data = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        self.n -= 1
        return data
    
    def __len__(self):
        return self.n
    
    def __contains__(self, data):
        p = self.first
        while p is not None:
            if p.data == data:
                return True
            p = p.next
        return False
        
class File(ListeChainee):
    def __init__(self):
        super().__init__()
        
    def insert(self, data):
        self.insert_last(data)
        
    def remove(self):
        return self.remove_first()
    
    
    def __str__(self):
        res = ''
        p = self.first
        while p is not None:
            res += str(p.data) + " <- "
            p = p.next
        res = res[:-4] # pour retirer la dernière flèche
        return res    
        


class Joueur:
    def __init__(self, pseudo, niveau = 1):
        self.pseudo = pseudo
        self.niveau = niveau
        self.xp = 0
        self.sante = 100
        self.x = 0
        
    def __str__(self):
        etat = ""
        if self.sante > 80:
            etat = "en pleine forme"
        elif self.sante > 50:
            etat = "fatigué"
        elif self.sante > 0:
            etat = "dans un sale état"
        else:   
            etat = "Mort (RIP)"
        return f"{self.pseudo} (Niveau: {self.niveau}) : {etat}"
    
    def __repr__(self):
        return f"{self.pseudo} | Niveau: {self.niveau} | XP: {self.xp} | Santé: {self.sante}"
     
    def name(self):
        return self.pseudo
 
    def set_sante(self, sante):
        self.sante = sante
        
    def get_sante(self):
        return self.sante
 
    def is_alive(self):
        return self.sante > 0
    
    def get_niveau(self):
        return self.niveau
 
    def seuil(self):
        return 10 * self.niveau
    
    def gagner_xp(self, points):
        self.xp += points
        level_up = False
        while self.xp >= self.seuil():
            self.xp -= self.seuil()
            self.niveau += 1
            self.sante = 100
            level_up = True
        return level_up     
          
    def degats(self):
        return self.niveau * 2
    
    def subir_degats(self, degats):
        degats = degats - self.resistance()
        if degats > 0:
            self.sante -= degats
        if self.sante <= 0:
            self.sante = 0
                    
    def attaquer(self, other):
        degats_infliges = self.degats()
        other.subir_degats(degats_infliges)
        level_up = self.gagner_xp(100)
        return level_up, degats_infliges
    
    def resistance(self):
        return self.x * self.niveau
        
    def __lt__(self, other):
        return (self.niveau, self.xp) < (other.niveau, other.xp)
    
    def __add__(self, other):
        return Joueur(f"{self.pseudo}+{other.pseudo}", self.niveau + other.niveau)


class Guerrier(Joueur):
    def __init__(self, pseudo, niveau = 1, force = 10):
        super().__init__(pseudo, niveau)
        self.force = force
        self.x = 1.4
            
    def __repr__(self):
        return super().__repr__() + f" | Force: {self.force}"      
        
    def degats(self):
        return super().degats() + self.force

class Mage(Joueur):
    def __init__(self, pseudo, niveau = 1, intelligence = 10):
        super().__init__(pseudo, niveau)
        self.intelligence = intelligence
        self.x = 1
                
    def __repr__(self):
        return super().__repr__() + f" | Intelligence: {self.intelligence}" 
                
    def lancer_sort(self, other: Joueur):
        degats_infliges = self.intelligence
        other.subir_degats(degats_infliges)
        level_up = self.gagner_xp(30)
        return level_up, degats_infliges

class Monstre(Joueur):
    def __init__(self, niveau=1):
        super().__init__("Monstre" + str(random.randrange(2000)), niveau)
        self.x = 0.3
        
    def gagner_xp(self, _):
        self.xp = 0
        return self.niveau
    
class Boss(Joueur):
    def __init__(self, niveau=1):
        super().__init__("Boss", niveau)
        self.x = 1.5
        self.barre_vie = 3
        
    def gagner_xp(self, _):
        self.xp = 0
        return self.niveau
    
    def subir_degats(self, degats_infliges):
        super().subir_degats(degats_infliges)
        if self.sante < 0:
            if self.barre_vie > 0:
                self.set_sante(100)
                self.barre_vie -= 1
            
    

class Donjon():
    def __init__(self):
        self.monsters = File()
        
        
    def generate_monsters(self, niveau):
        self.monsters = File()
        for i in range(max(niveau + random.randint(-3, 3), 1)):
            self.monsters.insert(Monstre(max(niveau + random.randint(-3, 3), 1)))
        if niveau % 5 == 0 and niveau != 0:
            self.monsters.insert(Boss(niveau))
            
    def fight(self, player: Joueur):
        self.generate_monsters(player.niveau)
        # On parcourt la liste des monstres
        monster_node = self.monsters.first
        while player.is_alive() and monster_node is not None:
            monster = monster_node.data
            
            # Combat contre le monstre tant qu'il est vivant
            while player.is_alive() and monster.is_alive():
                player.attaquer(monster)
                if monster.is_alive():
                    monster.attaquer(player)
                    
            # Si le monstre est mort, passer au suivant
            monster_node = monster_node.get_next()
        return player.is_alive()
    
    def __str__(self):
        return str(self.monsters)
        
donjon = Donjon()
Matis = Joueur("Matis", 1)
win = True
for i in range(2):
    win = donjon.fight(Matis)

print(win)
        
        