from cria_tabela2 import Model


modelo = Model("usuarios", "nome", "sobrenome")

modelo.create("Antonio", "Netto")
modelo.create("Joana", "Assis")
modelo.create("Juliana", "Alvarenga")

x = modelo.find_atribute("sobrenome", "Assis")

print(x)

x = modelo.find_atribute("sobrenome", "Assis")

print(x)