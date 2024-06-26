import csv
import pandas as pd
from colorama import Fore
def chercher_mot_dans_csv(nom_fichier, mot):
    try:
        with open(nom_fichier, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            result = []
            for row in reader:
                for cell in row:
                    if mot in cell:
                        print(f"{Fore.YELLOW}")
                        print(f"{Fore.BLUE}found one instance of '{Fore.CYAN}{mot}{Fore.BLUE}' in => \n{Fore.WHITE}{row}")
                        print(f"{Fore.WHITE}", end='')
                        print(f"{Fore.YELLOW}", end='')
                        print("row count : ", end='')
                        print(row.count)
                        print(f"{Fore.WHITE}")
        return f"Mot '{mot}' non trouvé dans le fichier."
    except FileNotFoundError:
        return f"Le fichier '{nom_fichier}' n'a pas été trouvé."
# settings
file_name = 'samples\\LGE_File config.csv'
search_keyword = '\\'
result = chercher_mot_dans_csv(file_name, search_keyword)
print(result)