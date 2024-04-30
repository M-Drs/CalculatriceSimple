from colorama import Fore, Style

def division_func(premier_nombre, deuxieme_nombre):
    if deuxieme_nombre == "0":
       return print(f"{Fore.RED}Division par 0 impossible !{Style.RESET_ALL}")
    else:
        return float(premier_nombre) / float(deuxieme_nombre)
        
    

if __name__ == "__main__":
    print(division_func(10,"4"))
    