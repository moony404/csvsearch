import csv
import pandas as pd
from colorama import Fore
def chercher_mot_dans_csv(file_name, search_keyword):
    try:
        with open(file_name, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            result = []
            for row in reader:
                for cell in row:
                    if search_keyword in cell:
                        print(f"{Fore.YELLOW}")
                        print(f"{Fore.BLUE}found one instance of '{Fore.CYAN}{search_keyword}{Fore.BLUE}' in => \n{Fore.WHITE}{row}")
                        print(f"{Fore.WHITE}", end='')
                        print(f"{Fore.YELLOW}", end='')
                        print("row count : ", end='')
                        print(row.count)
                        print(f"{Fore.WHITE}")
        return f"Mot '{search_keyword}' non trouvé dans le fichier."
        print(f"{Fore.BLUE}[notice] {Fore.YELLOW}The word {Fore.WHITE}'{search_keyword}'{Fore.YELLOW} wasn't found.{Fore.WHITE}")
    except FileNotFoundError:
        print(f"{Fore.BLUE}[{Fore.RED}error{Fore.BLUE}] {Fore.YELLOW}The file {Fore.WHITE}'{file_name}'{Fore.YELLOW} wasn't found.{Fore.WHITE}")
# settings
file_name = 'samples\\LGE_File config.csv'
search_keyword = '\\'
result = chercher_mot_dans_csv(file_name, search_keyword)
print(result)