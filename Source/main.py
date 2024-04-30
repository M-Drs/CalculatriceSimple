# Import
import sys
from fireworks import fireworks
import emoji
from dotenv import load_dotenv
from code_source_calculatrice import run_calculatrice
from code_source_calculatrice import input_choix_utilistaeur
from code_source_calculatrice import choix_utilisateur_affichage
import os
load_dotenv()

MDP = os.getenv('MOT_DE_PASSE')
mdp = input('Mot de passe?')
if mdp == MDP :
    print(fireworks(True))
else :
    print(fireworks(False))
    sys.exit()

# Menu calculatrice
menu = """1- (+) Addition
2- (-) Soustraction
3- (x) Multiplication
4- (:) Division
5- (q) Quitter
Votre choix : """

phrase_premier_nombre = "Entrez le premier nombre : "
phrase_deuxieme_nombre = "Entrez le deuxieme nombre : "


# Choix possible
choix_possible = ["1", "2", "3", "4", "q"]
choix_utilisateur = None
continuer = "o"

if __name__ == "__main__":
    choix_utilisateur = input_choix_utilistaeur(menu)
    premier_nombre, deuxieme_nombre = choix_utilisateur_affichage(choix_utilisateur, choix_possible, phrase_premier_nombre, phrase_deuxieme_nombre)
    run_calculatrice(premier_nombre, deuxieme_nombre, choix_utilisateur)