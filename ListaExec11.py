"""
IPEA - Mestrado em Políticas Públicas e Desenvolvimento
3a. turma
Prof. Bernardo Furtado

Aluna: Sissi Alves da Silva

1a Lista de Exercícios

11. Escreva uma função que recebe uma lista e organiza os valores em keys e conta a frequência
de cada uma. Por exemplo: a lista [0, 0, 1, 1, 1, 2, 5], resultaria em: {1: 3, 0: 2, 2: 1, 5: 1}.
"""

def histograma(lista):
    lista2 = lista
    lista3 = {}
    count = 0
    for each in lista2:
        for each in lista:
            
            count = count + 1
            lista3[(count)] = [(each)]


    print(lista3)

if __name__ == '__main__':

    l = [0, 0, 1, 1, 1, 2, 5]
    histograma(l)

