"""
IPEA - Mestrado em Políticas Públicas e Desenvolvimento
3a. turma
Prof. Bernardo Furtado

Aluna: Sissi Alves da Silva

1a Lista de Exercícios

1. Escreva um programa que ache os números divisíveis por 7 e por 13, entre o seu ano de
nascimento e 2701.
"""

#Percorrer todos os números entre 1977 e 2701 (inclusive)

def func_numbers():
    for i in range(1977, 2702):
        if 0 == i % 7 and 0 == i % 13:  # se for divisível por 7 e 13
            print('{} é divisível por 7 e 13'.format(i))  # imprime os números

if __name__ == '__main__':
    func_numbers()

#funcionando SAS