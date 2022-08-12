def decora_funcao(func):
    def decoracao(*colunas):
        vares = len(colunas)
        
        
        func()
        

    return decoracao






@decora_funcao
def funcaoprincipal():
    print('centrro da função')



funcaoprincipal()