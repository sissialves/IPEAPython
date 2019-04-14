"""
IPEA - Mestrado em Políticas Públicas e Desenvolvimento
3a. turma
Prof. Bernardo Furtado

Aluna: Sissi Alves da Silva

1a Lista de Exercícios

4. Escreva um programa que corre os números de 1 a 50 e imprime. Mas, quando for múltiplo
de três, imprima ‘Oops’, quando for múltiplo de 5 imprima ‘Doo’, quando for de ambos
imprima ‘OopsDoo’..
"""

#Percorrer todos os números entre 1 a 50 (inclusive)
def print_numbers():
    for i in range(1977, 2702):
        if 0 == i % 3:  # se for divisível por 3
            print('Oops {} é divisível por 3'.format(i))  #imprime os números divisíveis por 3.
        if 0 == i % 5:  # se for divisível por 5
            print('Doo {} é divisível por 5'.format(i))  # imprime os números divisíveis por 5.
        if 0 == i % 3 and 0 == i % 5:  # se for divisível por 3 e 5
            print('OopsDoo {} é divisível por 3 e por 5'.format(i))  # imprime os números divisíveis por 3 e 5.

if __name__ == '__main__':
    print_numbers()


