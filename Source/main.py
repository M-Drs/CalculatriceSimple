
# Import
from colorama import Fore, Style
import sys
from division import division_func
from multiplication import multiplication_func
from addition import addition
from soustraction import soustraction



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

    print("-" * 20)
    choix_utilisateur = input(menu)

    if choix_utilisateur not in choix_possible:
        print("Veuillez choisir une option valide...")
        continue

    if choix_utilisateur == "q":
        sys.exit()


    premier_nombre = input(phrase_premier_nombre)
    deuxieme_nombre = input(phrase_deuxieme_nombre)
    

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

            print(f"{premier_nombre} divisé par {deuxieme_nombre} = {division}")

            
            
l1=r"                                   .''.       "
l2=r"       .''.      .        *''*    :_\/_:     . "
l3=r"      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'."
l4=r"  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-"
l5=r" :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'."
l6=r" : /\ : :::::     *_\/_*     -= o =-  /)\    '  *"
l7=r"  '..'  ':::'     * /\ *     .'/.\'.   "
l8=r"      *            *..*         :"

print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print(l6)
print(l7)
print(l8)

