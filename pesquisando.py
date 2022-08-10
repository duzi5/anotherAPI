import os
import json


pasta = './dados'

def pesquisar(pasta, categoria, valor_pesquisado):
    for arquivo in os.walk(pasta):
        print(arquivo[2])
        for arquivo in arquivo[2]:
            caminho_arquivo = pasta + '/' + arquivo 
            with open(caminho_arquivo, 'r') as arquiv:
                x = json.load(arquiv)
                print(x)
                if x[categoria] == valor_pesquisado:
                    return arquiv
            

            
            
pesquisar(pasta, 'idade', 30)