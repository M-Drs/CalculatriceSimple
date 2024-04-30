# Import
from colorama import Fore, Style
import sys
from division import division_func
from multiplication import multiplication_func
from addition import addition
from soustraction import soustraction
from fireworks import fireworks
import emoji
from dotenv import load_dotenv
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


# Gestion des erreurs
# division par 0 ? 
# Si entrée invalide -> Message



while continuer == "o":

  

    choix_utilisateur = input(menu)

    if choix_utilisateur not in choix_possible:
        print(f"{Fore.RED}Veuillez choisir une option valide...{Style.RESET_ALL}")
        continue

    else:

        if choix_utilisateur == "q":
                sys.exit()

        premier_nombre = input(phrase_premier_nombre)
        deuxieme_nombre = input(phrase_deuxieme_nombre)

        if  premier_nombre.isdigit() and deuxieme_nombre.isdigit():
            

            if choix_utilisateur == "1":
                # Code addition
                addition_result = addition(premier_nombre, deuxieme_nombre)
                print(f"{Fore.GREEN}{premier_nombre} + {deuxieme_nombre} = {addition_result}{Style.RESET_ALL}")

            elif choix_utilisateur == "2":
                # Code soustraction
                soustraction_result = soustraction(premier_nombre, deuxieme_nombre)
                print(f"{Fore.GREEN}{premier_nombre} - {deuxieme_nombre} = {soustraction_result}{Style.RESET_ALL}")
                

            elif choix_utilisateur == "3":
                # Code Multiplication
                multiplication = multiplication_func(premier_nombre=premier_nombre, deuxieme_nombre=deuxieme_nombre)
                print(f"{Fore.GREEN}{premier_nombre} x {deuxieme_nombre} = {multiplication}{Style.RESET_ALL}")

            elif choix_utilisateur == "4":
                # Code Division
                division = division_func(premier_nombre=premier_nombre, deuxieme_nombre=deuxieme_nombre)
                print(f"{Fore.GREEN}{premier_nombre} / {deuxieme_nombre} = {division}{Style.RESET_ALL}")
        
        else:
            print(f"{Fore.RED}Entrée non valide !{Style.RESET_ALL}")