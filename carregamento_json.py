import json 


current_user = 3349543233445

nome_arq = current_user



with open(f'dados/{nome_arq}.json', 'r') as arquivo:
    current_dados = json.load(arquivo) 

