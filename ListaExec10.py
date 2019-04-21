"""
IPEA - Mestrado em Políticas Públicas e Desenvolvimento
3a. turma
Prof. Bernardo Furtado

Aluna: Sissi Alves da Silva

1a Lista de Exercícios

10. Escreva uma função que retorna os máximos e mínimos de um dicionário.
"""


def valormaximo(numero):
    maximo = max(numero, key=numero.get)

    return numero[maximo]


def valorminimo(numero):
    minimo = min(numero, key=numero.get)

    return numero[minimo]

if __name__ == '__main__':

    dicionario = {"n1": 1, "n2": 2, "n3": 3, "n4":4, "n5":5 }

    print("O dicionário é:",dicionario)

    print("O valor mínimo do dicionário é:",valorminimo(dicionario))

    print("O valor máximo do dicionário é:",valormaximo(dicionario))

#funcionando SAS