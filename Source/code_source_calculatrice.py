from colorama import Fore, Style
from colorama import Fore, Style
import sys
from division import division_func
from multiplication import multiplication_func
from addition import addition
from soustraction import soustraction



def input_choix_utilistaeur(menu):
    choix_utilisateur = input(menu)
    return choix_utilisateur


def choix_utilisateur_affichage(choix_utilisateur, choix_possible, phrase_premier_nombre, phrase_deuxieme_nombre):

    if choix_utilisateur not in choix_possible:
            print(f"{Fore.RED}Veuillez choisir une option valide...{Style.RESET_ALL}")  
    else:

        if choix_utilisateur == "q":
                sys.exit()

    premier_nombre = input(phrase_premier_nombre)
    deuxieme_nombre = input(phrase_deuxieme_nombre)

    return premier_nombre, deuxieme_nombre


def run_calculatrice(premier_nombre, deuxieme_nombre, choix_utilisateur):

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