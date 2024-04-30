# Fonction soustraction fait pas Guilhem
import math

def soustraction(premier_nombre: float, deuxieme_nombre: float):
    return round((float(premier_nombre) - float(deuxieme_nombre)), 1)

if __name__ == "__main__":
    print(soustraction(3.4, 3.2))