# Import
import sys
from fireworks import fireworks
import emoji
from dotenv import load_dotenv
from code_source_calculatrice import run_calculatrice
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



# Choix possible
choix_possible = ["1", "2", "3", "4", "q"]
choix_utilisateur = None
continuer = "o"

if __name__ == "__main__":
    run_calculatrice(menu, choix_possible)