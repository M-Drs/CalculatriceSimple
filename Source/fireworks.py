import emoji
from colorama import Fore, Style
def fireworks(accord):
    
    l1=r"                                   .''.       "
    l2=r"       .''.      .        *''*    :_\/_:     . "
    l3=r"      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'."
    l4=r"  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-"
    l5=r" :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'."
    l6=r" : /\ : :::::     *_\/_*     -= o =-  /)\    '  *"
    l7=r"  '..'  ':::'     * /\ *     .'/.\'.   "
    l8=r"      *            *..*         :"

    if accord == True: 
             
        return emoji.emojize(f"':party_popper::party_popper::party_popper: {Fore.RED} WELCOME {Style.RESET_ALL} :party_popper::party_popper::party_popper:'")+ "\n"+f"{Fore.GREEN}{l1}{Style.RESET_ALL}"+"\n"+f"{Fore.GREEN}{l2}{Style.RESET_ALL}"+"\n"+f"{Fore.YELLOW}{l3}{Style.RESET_ALL}"+"\n"+f"{Fore.YELLOW}{l4}{Style.RESET_ALL}"+"\n"+f"{Fore.GREEN}{l5}{Style.RESET_ALL}"+"\n"+f"{Fore.CYAN}{l6}{Style.RESET_ALL}"+"\n"+f"{Fore.CYAN}{l7}{Style.RESET_ALL}"+"\n"+f"{Fore.MAGENTA}{l8}{Style.RESET_ALL}"

    

    else :
         return emoji.emojize(f"{Fore.RED} 💀💀 Mot de passe incorrect: La calculette se ferme {Style.RESET_ALL} 💀💀")


if __name__ == "__main__":
    print(fireworks(True))