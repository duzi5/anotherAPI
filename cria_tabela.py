import json



class CriaModel: 
    def __init__(self):    
        self.columns = [] 
        self.instance = {}
    
    def Column(self, name):
        self.columns.append(Coluna(name))
    
    def show_columns(self):
        for column in self.columns:
            print(column.name)
    
    def objOF(self, valores):
        obj = InstanceList(valores)
        return obj 

    def dictOf(self, values):
        d = {}
        d = dict(zip(values, self.columns))
        print(d)       
        return d
    

class Coluna: 
    def __init__(self, name):
        self.name = name
        self.valor = 0

class InstanceList:
    instance = []
    def __init__(self, values):
        for value in values:
            instance.append(value)
        return instance


modelo = CriaModel()

modelo.Column('nome')
modelo.Column('idade')
modelo.Column('numero')
modelo.Column('ingles')

modelo.show_columns()


individuo1 = modelo.objOF(["antonio", 12, 34, "yes"])

print(individuo1)



