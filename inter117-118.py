"""
Exercicio : 
Criar funções que duplicam, triplicam e quadruplicam o número recebido
como parâmentro
"""

def criar_multiplicador(multiplicador):
    def multiplicador(numero):
        return numero * multiplicador
    return multiplicador

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar)
print(triplicar)
print(quadruplicar)