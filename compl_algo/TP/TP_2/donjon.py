from umonsDS import Pile, File
from randomPlayer import new_player
from random import random, choice
from joueur import *

boss = Joueur("Blind Guardian", 20)
boss.set_sante(1000)

queue = File() # file d'attente des joueurs, devant le donjon
defeated = Pile() # pile des joueurs vaincus
fighting = [] # liste des joueurs en combat
MAX = 3 # nombre maximum de joueurs en combat


t = 0
while True:
    t += 1
    print(f"TOUR {t}".center(50, '*'))

    # arrivée aléatoire de nouveaux joueurs
    print()
    print("DEVANT LE DONJON".center(50, '='))
    if len(queue) == 0:
        p = new_player()
        print(f"Arrivée de {p}")
        queue.insert(p)
    for _ in range(2):
        if random() < 0.25:
            p = new_player()
            print(f"Arrivée de {p}")
            if len(queue) < 10:
                queue.insert(p)
            else:
                print(f"{p.name()} repart déçu, il y a trop de monde devant le donjon")
    print("Il y a", len(queue), "personnages qui attendent devant le donjon\n")
    
    print("DANS LE DONJON".center(50, '='))
    # entrée des joueurs dans le donjon
    nb = MAX - len(fighting)
    for _ in range(nb):
        if len(queue) == 0:
            break
        p = queue.remove()
        print(f"Entrée dans le donjon de {p.name()}")
        fighting.append(p)
    print()
        
    # combats
    print('   ', "ATTAQUE DES AVENTURIERS".center(44, '-'))
    for p in fighting:
        lvl, dg = p.attaquer(boss)
        print(f"{p.name()} attaque {boss.name()} et lui inflige {dg} points de dégâts")
        if lvl:
            print(f"{p.name()} passe au niveau {p.get_niveau()}")
        if isinstance(p, Mage):
            lvl, dg = p.lancer_sort(boss)
            print(f"{p.name()} lance une boule de feu sur {boss.name()} et lui inflige {dg} points de dégâts")
            if lvl:
                print(f"{p.name()} passe au niveau {p.get_niveau()}")
        if not boss.is_alive():
            print(f"!!! Incroyable {boss.name()} est mort !!!")
            lvl = p.gagner_xp(1000)
            print(f"{p.name()} gagne 1000 points d'expérience")
            if lvl:
                print(f"{p.name()} atteint le niveau {p.get_niveau()}")
            p.set_sante(1000)
            print(f"Avec un rire démonique, {p.name()} retrouve une santé de fer")
            print(f"en prenant l'amulette maléfique de {boss.name()}")
            print(f"{p.name()} devient le nouveau boss du Donjon !")
            defeated.push(boss)
            boss = p
            fighting.remove(p)
    
    print()
    print('   ', f"Réaction de {boss.name()}".upper().center(44, '-'))
    if len(fighting) > 0:
        victim = choice(fighting)
        lvl, dg = boss.attaquer(victim)
        print(f"{boss.name()} attaque {victim.name()} et lui inflige {dg} points de dégâts")
        if lvl:
            print(f"{boss.name()} passe au niveau {boss.get_niveau()}")
        if not victim.is_alive():
            print(f"{victim.name()} est mort")
            defeated.push(victim)
            fighting.remove(victim)
    print()
    print('   ', "ETAT DES AVENTURIERS DANS LE DONJON".center(44, '-'))
    print('En vie:')
    for p in fighting:
        print('  ', p)
    if len(defeated) > 0:
        print("Il y a aussi un tas de", len(defeated), "aventuriers vaincus derrière", boss.name())
        if random() < 0.3:
            print(f"{boss.name()} a faim et mange {defeated.get_top().name()} qui se trouve en haut de ce tas")
            defeated.pop()
            print(f"{boss.name()} regagne des PV")
            boss.set_sante(min(1000, boss.get_sante() + 50))
    
    print()
    print('   ', f"ETAT DE {boss.name()}".upper().center(44, '-'))
    print(str(boss) + ' (' + str(boss.get_sante()) + ' PV)')
    print()
    ans = input("Appuyez sur Entrée pour continuer... (Q pour quitter, V pour voir les SD) ")
    if ans.lower() == 'v':
        print("\nFile devant le donjon:")
        print(queue)
        print("\nAventuriers dans le donjon:")
        for p in fighting:
            print(p)
        print("\nTas des aventuriers vaincus:")
        print(defeated) 
        ans = input("Appuyez sur Entrée pour continuer... (Q pour quitter) ")
        if ans.lower() == 'q':
            break
    if ans.lower() == 'q':
        break