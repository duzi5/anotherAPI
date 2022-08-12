import json

class Model():
    def __init__(self, *colunas):
        self.colunas = colunas
        self.dici = []

    def create(self, *valores):
        self.dici = dict(zip(self.colunas, valores))
        print(self.dici )
        return self.dici

    def update(self, chave, valor):
        self.dici[chave] = valor
    
    def delete_all(self):
        self.dici.clear()

    def gera_arq(self):
        jason = json.dumps(self.dici, indent=4) 
        nome_arq = 1290130923
        with open(f'testes/{nome_arq}.json', 'w') as arquivo:
            arquivo.write(jason)
    
    


modelo = Model("nome", "sobrenome")


modelo.create("antonio", "netto")

modelo.gera_arq()