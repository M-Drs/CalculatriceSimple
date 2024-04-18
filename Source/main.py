# Import
from colorama import Fore, Style
import sys
from division import division_func
from multiplication import multiplication_func
from addition import addition
from soustraction import soustraction
import emoji
from dotenv import load_dotenv
import os
load_dotenv()

MDP = os.getenv('MOT_DE_PASSE')
mdp = input('Mot de passe?')
if mdp == MDP :
    print("-" * 20)

    l1=r"                                   .''.       "
    l2=r"       .''.      .        *''*    :_\/_:     . "
    l3=r"      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'."
    l4=r"  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-"
    l5=r" :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'."
    l6=r" : /\ : :::::     *_\/_*     -= o =-  /)\    '  *"
    l7=r"  '..'  ':::'     * /\ *     .'/.\'.   "
    l8=r"      *            *..*         :"

    print(emoji.emojize(f"':party_popper::party_popper::party_popper: {Fore.RED} WELCOME {Style.RESET_ALL} :party_popper::party_popper::party_popper:'"))
    print(f"{Fore.GREEN}{l1}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{l2}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{l3}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{l4}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{l5}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{l6}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{l7}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}{l8}{Style.RESET_ALL}")

else :
    print(emoji.emojize(f"{Fore.RED} 💀💀 Mot de passe incorrect: La calculette se ferme {Style.RESET_ALL} 💀💀"))
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
                addition_result = addition(premier_nombre, deuxieme_nombre)
                print(f"{Fore.GREEN}{premier_nombre} + {deuxieme_nombre} = {addition_result}{Style.RESET_ALL}")

            elif choix_utilisateur == "2":
                soustraction_result = soustraction(premier_nombre, deuxieme_nombre)
                print(f"{Fore.GREEN}{premier_nombre} - {deuxieme_nombre} = {soustraction_result}{Style.RESET_ALL}")
                

            elif choix_utilisateur == "3":
                # Code Multiplication
                multiplication = multiplication_func(premier_nombre=premier_nombre, deuxieme_nombre=deuxieme_nombre)
                print(f"{Fore.GREEN}{premier_nombre} x {deuxieme_nombre} = {multiplication}{Style.RESET_ALL}")

            elif choix_utilisateur == "4":
                # Code Division
                if deuxieme_nombre == "0":
                    print(f"{Fore.RED}Division par 0 impossible !{Style.RESET_ALL}")
                else:
                    division = division_func(premier_nombre=premier_nombre, deuxieme_nombre=deuxieme_nombre)

                    print(f"{Fore.GREEN}{premier_nombre} / {deuxieme_nombre} = {division}{Style.RESET_ALL}")
        
        else:
            print(f"{Fore.RED}Entrée non valide !{Style.RESET_ALL}")