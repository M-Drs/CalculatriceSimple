# Guilhem travail sur la fonction addition
# from colorama import Fore, Style : pour faire des couleurs f"{Fore.GREEN}RESULTAT:{Style.RESET_ALL}"


def addition(nombre1: float, nombre2: float):
    """_summary_

    Args:
        nombre1 (float): un nombre de type float
        nombre2 (float): un nombre de type float

    Returns:
        float : l'addition de nombre1 et nombre2
    """
    return float(nombre1) + float(nombre2)


if __name__ == "__main__":
    print(addition("10",10))
    