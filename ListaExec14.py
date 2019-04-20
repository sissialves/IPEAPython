"""
IPEA - Mestrado em Políticas Públicas e Desenvolvimento
3a. turma
Prof. Bernardo Furtado

Aluna: Sissi Alves da Silva

1a Lista de Exercícios
14. Escreva um programa que verifica se todas as letras do alfabeto constam no mínimo uma
vez do parágrafo fornecido pelo usuário.
"""
from string import ascii_letters


def check_alphabet(paragraph):
    gabarito = ascii_letters
    tamanho = (len(gabarito))/2
    count = 0

    for each in gabarito:
        if each in paragraph:
            count = count + 1
        else:
            continue
    if count >= tamanho:
        print('PANAGRAMA')
    else:
        print('Não é PANAGRAMA')

if __name__ == '__main__':

    frase = input('Digite uma frase: ')
    check_alphabet(frase)

#teste de novo