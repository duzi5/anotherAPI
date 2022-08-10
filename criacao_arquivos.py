import json 


current_user = 334954325675678777


class Pessoa:
    def __init__(self, nome, idade, ingles, nota):
        self.nome = nome 
        self.idade = idade
        self.ingles = ingles
        self.nota = nota
    

    def json(self): 
        conteudo = ' "nome" : "{}",   "idade" : "{}" , "ingles" : "{}", "nota" : "{}"' .format( self.nome, self.idade, self.ingles, self.nota )  
        return '{' + f'{conteudo}' + '}'
nome_arq = current_user
pessoa1 = Pessoa('rebeca', 20, True, 11)

with open(f'dados/{nome_arq}.json', 'w') as arquivo:
    arquivo.write(pessoa1.json())    
