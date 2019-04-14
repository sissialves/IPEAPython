"""
IPEA - Mestrado em Políticas Públicas e Desenvolvimento
3a. turma
Prof. Bernardo Furtado

Aluna: Sissi Alves da Silva

1a Lista de Exercícios


8.Dicionários. Dado o dicionário: d = {‘a’: 0}: faça programas que 8.1 acrescente um par
(chave, valor) {‘b’: 1}, ao dicionário; 8.2 verifique se a key ‘c’ está presente? 8.3
Concatene um dicionário a um outro dicionário: e = {z : 23}. Use o método ‘update’!
"""


def acrescente(d1):
    dict2 = d1
    dict2.update({'b': 1})
    print(dict2)
    return dict2


if __name__ == 'main':

    dict1 = {}
    dict1.update = {'a': 0}

    acrescente(dict1)
    print('Meu novo dicionário', dict1)