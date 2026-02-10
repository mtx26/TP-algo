def belongs_to_dictionary(word):
	"""
	Vérifie si le mot donné se trouve dans le fichier de dictionnaire.
	Paramètres:
	- word (str): le mot à rechercher.
	Retour:
	- bool: True si le mot est présent dans le fichier 'TP_5/words.txt', sinon False.
	"""
	with open('TP_5/words.txt', "r") as fichier:
		word.lower()
		find = False
		for line in fichier:
			dic = line.strip()
			if word == dic:
				find = True
				return find
		if find == False:
			return find
		
def ask_word_in_dictionary():
	"""
	Demande à l'utilisateur de saisir un mot qui appartient au dictionnaire.
	La fonction boucle jusqu'à ce que l'utilisateur entre un mot présent dans le fichier de dictionnaire.
	Retour:
	- str: le mot saisi et validé.
	"""
	correct = False
	while correct == False:
		word = input("Enter a word : ")
		word.lower()
		if belongs_to_dictionary(word):
			correct = True
			return word
		else:
			print("this word does not belong to the dictionnary for that hangman !! Try another one...")

def ask_letter(tried_letters):
	"""
	Demande à l'utilisateur de saisir une lettre (un seul caractère) qui n'a pas encore été essayée.
	Paramètres:
	- tried_letters (list): liste des lettres déjà tentées.
	Retour:
	- str: la lettre saisie par l'utilisateur.
	"""
	correct = False
	while correct == False:
		letter = input("Enter your guess : ")
		if len(letter) == 1:
			found = False
			for l in tried_letters:
				if l == letter:
					found = True
			if found:
				print("you already guessed that one !")
			else:
				correct = True
				return letter
		else:
			print("Only one letter per guess !")

def is_the_letter_in_the_word(word, tried_letters):
	"""
	Vérifie si la lettre saisie par l'utilisateur fait partie du mot.
	Paramètres:
	- word (str): le mot à deviner.
	- tried_letters (list): liste des lettres déjà tentées (sera utilisée par ask_letter).
	Retour:
	- (bool, str): tuple où le premier élément est True si la lettre est dans le mot, False sinon;
	  le second élément est la lettre testée.
	"""
	l = ask_letter(tried_letters)
	for letter in word:
		if l == letter:
			return True, l
	return False, l

def display_word(word, tried_letters):
	"""
	Construit et renvoie la représentation du mot en remplaçant les lettres non trouvées par des '*'.
	Paramètres:
	- word (str): le mot à afficher.
	- tried_letters (list): lettres déjà trouvées ou tentées.
	Retour:
	- str: la chaîne affichée avec lettres découvertes et '*' pour les lettres non découvertes.
	"""
	display_word = ""
	for l in word:
		if l in tried_letters:
			display_word += l
		else:
			display_word += "*"
	return display_word

def if_word_is_guessed(word, tried_letters):
	"""
	Vérifie si toutes les lettres du mot ont été devinées.
	Paramètres:
	- word (str): le mot à vérifier.
	- tried_letters (list): lettres déjà tentées.
	Retour:
	- bool: True si toutes les lettres du mot sont présentes dans tried_letters, sinon False.
	"""
	display_word = ""
	for l in word:
		if l in tried_letters:
			display_word += l
	return display_word == word


if __name__ == "__main__":
	print(display_word("salut", ["a", "b", "c"]))
