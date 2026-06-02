
def price_func() : 
    prix = input('Veuillez entrer le prix de votre artcile (Tous nos prix sont ronds !): ')
    if prix.isdigit() :
        prix = int(prix)
        return prix
    else :
        print('Il ne s\'agit pas d\'un prix... Veuillez recommencer.')
        exit()


def billets20() :
    b20 = input('Veuillez indiquer combien de billet(s) de 20 vous souhaitez déposer : ')
    if b20.isdigit() :
        b20 = int(b20)
        return b20
    else :
        print('Vous n\'avez pas entré un nombre... Veuillez recommencer.')
        exit()

def billets10() :
    b10 = input('Veuillez indiquer combien de billet(s) de 10 vous souhaitez déposer : ')
    if b10.isdigit() :
        b10 = int(b10)
        return b10
    else :
        print('Vous n\'avez pas entré un nombre... Veuillez recommencer.')
        exit()


def billets5() :
    b5 = input('Veuillez indiquer combien de billet(s) de 5 vous souhaitez déposer : ')
    if b5.isdigit() :
        b5 = int(b5)
        return b5
    else :
        print('Vous n\'avez pas entré un nombre... Veuillez recommencer.')
        exit()

def pieces2() :
    p2 = input('Veuillez indiquer combien de pièces de 2 vous souhaitez déposer : ')
    if p2.isdigit() :
        p2 = int(p2)
        return p2
    else :
        print('Vous n\'avez pas entré un nombre... Veuillez recommencer.')
        exit()

def pieces1() :
    p1 = input('Veuillez indiquer combien de pièces de 1 vous souhaitez déposer : ')
    if p1.isdigit() :
        p1 = int(p1)
        return p1
    else :
        print('Vous n\'avez pas entré un nombre... Veuillez recommencer.')
        exit()


def rendreMonnaie(price_func, billets20, billets10, billets5, pieces2, pieces1) :
    price = price_func()
    monnaie = (20*billets20() + 10*billets10() + 5*billets5() + 2*pieces2() + pieces1()) - price
    if monnaie < 0 :
        print('Il n\'a pas assez d\'argent, veuillez recommencer.')
        exit()
    else :
        y1 = monnaie // 20
        y2 = (monnaie % 20) //10
        y3 = (monnaie % 10) // 5
        y4 = (monnaie % 5) // 2
        y5 = monnaie % 5 % 2
        return ('Il faut rendre '+str(y1) + ' billet(s) de 20, '+ str(y2)+' billet(s) de 10, '+ str(y3)+ ' billets de 5, '+ str(y4) + ' pièce(s) de 2 et '+ str(y5)+ ' pièce(s) de 1. Soit '+ str(monnaie) + ' euros.')



print(rendreMonnaie(price_func, billets20, billets10, billets5, pieces2, pieces1))


