"""
IPEA - Mestrado em Políticas Públicas e Desenvolvimento
3a. turma
Prof. Bernardo Furtado

Aluna: Sissi Alves da Silva

1a Lista de Exercícios

11. Escreva uma função que recebe uma lista e organiza os valores em keys e conta a frequência
de cada uma. Por exemplo: a lista [0, 0, 1, 1, 1, 2, 5], resultaria em: {1: 3, 0: 2, 2: 1, 5: 1}.
"""

def hist(lteste):

#dicionário que vai armazenar o número(chave do dicionário) e quantas vezes ele aparece na lista(valor)

    dicionario = {}
    for each in lteste:
        dicionario[each] = dicionario.get(each, 0) + 1

    return dicionario


if __name__ == '__main__':
    listateste = [0, 0, 1, 1, 1, 2, 5]

    print("A lista teste é: ",listateste)
    print("O histograma da lista teste é: ",hist(listateste))

#funcionando SAS

