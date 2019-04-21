"""
IPEA - Mestrado em Políticas Públicas e Desenvolvimento
3a. turma
Prof. Bernardo Furtado

Aluna: Sissi Alves da Silva

1a Lista de Exercícios

7. Escreva um programa que, dada uma lista de números [2, 34, 5, 6, 5, 4, 32] qualquer,
retorne: o primeiro valor, o número de valores, o último valor, a soma, a média e a mediana.
Obs. Para listas com tamanho ímpar, a mediana é o valor do meio, quando ordenada
(sorted()). Para listas pares, os dois valores do meio.
"""


def primeirovalor(ln):
    #retorna primeiro valor
    n1 = ln[0]
    return n1

def qtdadevalores(ln):
    #calcula o comprimento da lista
    n2 = len(ln)
    return n2

def ultimovalor(ln):
    # retorna o último valor da lista
    n3 = ln[len(ln)-1]
    return n3

def somavalores(ln):
    # soma os valores da lista
    n4 = sum(ln)
    return n4

def mediavalores(ln):
    # calcula a media dos valores da lista
    n5 = sum(ln)/len(ln)
    return(n5)

def mediana(ln):
    # ordena a lista
    ln.sort()
    n6 = len(ln)
    meiolen = int(n6/2)

    if n6%2 != 0:
    # se tamanho da lista for ímpar, mediana é o valor central
        n7 = ln[meiolen]
    # se tamanho da lista é par, calcula média dos dois valores centrais
    else:
        n7 = (ln[meiolen - 1] + meiolen) / 2

    return n7

if __name__ == '__main__':

    listanum = [2, 34, 5, 6, 5, 4, 32]

    print('O primeiro valor da lista é:', primeirovalor(listanum))

    print('A lista tem {} valores:'.format(qtdadevalores(listanum)))

    print('O último valor da lista é:', ultimovalor(listanum))

    print('A soma dos valores da lista é:', somavalores(listanum))

    print('A média dos valores da lista é:', mediavalores(listanum))

    print('A mediana dos valores da lista é:', mediana(listanum))

#funcionando SAS