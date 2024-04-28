import tkinter as tk
from tkinter import messagebox
from addition import addition
from soustraction import soustraction
from multiplication import multiplication_func
from division import division_func


def calculer():
    
    try:
        premier_nombre_input = float(premier_nombre.get())
        deuxieme_nombre_input = float(deuxieme_nombre.get())
        operation_a_effectuer = operateur.get()

        if operation_a_effectuer == "+":
            resultat = addition(premier_nombre_input, deuxieme_nombre_input)

        elif operation_a_effectuer == "-":
            resultat = soustraction(premier_nombre_input, deuxieme_nombre_input)

        elif operation_a_effectuer == "*":
            resultat = multiplication_func(premier_nombre_input, deuxieme_nombre_input)

        elif operation_a_effectuer == "/":

            if deuxieme_nombre_input == 0 :
                messagebox.showerror("Erreur", "Division par Zéro impossible")
                return
            else:
                resultat = division_func(premier_nombre_input, deuxieme_nombre_input)
        else:
            messagebox.showerror("Erreur", "Opération invalide !!")

        resultat_affichage.config(text="Résultat: " + str(resultat))
    except ValueError:
        messagebox.showerror("Erreur", "Opération invalide, entrez des valeurs numériques !!")





if __name__ == "__main__":

    root = tk.Tk()
    root.title("CalculatriceSimple")

    # Entrée 01 : premier nombre
    premier_nombre = tk.Entry(root)
    premier_nombre.grid(row=0, column=0, padx=5, pady=5)

    # Entrée 02 : deuxième nombre
    deuxieme_nombre = tk.Entry(root)
    deuxieme_nombre.grid(row=0, column=1, padx=5, pady=5)


    # Les opérateurs
    operateur = tk.StringVar()
    operateur.set("+") # opérateur par défault


    # la liste des opérateur
    operateurs_liste = tk.OptionMenu(root, operateur, "+", "-", "*", "/")
    operateurs_liste.grid(row=0, column=2, padx=5, pady=5)

    # Boutton calculer
    boutton_calculer = tk.Button(root, text="Calculer", command= calculer)
    boutton_calculer.grid(row=1, columnspan=3, padx=5, pady=5)

    # Afficher resultat
    resultat_affichage = tk.Label(root, text="Resultat:")
    resultat_affichage.grid(row=2, columnspan=3, padx=5, pady=5)

    root.mainloop()