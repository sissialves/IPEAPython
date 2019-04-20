"""
IPEA - Mestrado em Políticas Públicas e Desenvolvimento
3a. turma
Prof. Bernardo Furtado

Aluna: Sissi Alves da Silva

1a Lista de Exercícios
9. Escreva uma função que faz um loop as keys de um dicionário. Se as keys forem vogais,
eleve o valor ao quadrado. Caso contrário, set o valor para 0. Use if k in ‘aeiou’.
"""

def vowel(l):
    temp = {}
    Letras = 'aeiouAEIOU'

    chaves = l.keys()

    for cada in chaves:
        if cada not in Letras:
            temp[(cada)]= (l.get(cada))
        else:
            temp[(cada)]= (l.get(cada))**2

    return temp

if __name__ == '__main__':

    listel = {'a':2, 'b':4,'cc':6, 'o':30}


    print('O dicionário inicial é:',listel)
    print('O novo dicionário é:',vowel(listel))

#funcionando! SAS