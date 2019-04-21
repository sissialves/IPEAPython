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

#Pangrama, ou pantograma é uma frase em que são usadas todas as letras do alfabeto de determinada língua.

#Digitar frase teste: Bancos fúteis pagavam-lhe queijo, whisky e xadrez.
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
        print('A frase digitada é um PANGRAMA.')
        print('Pangrama, ou pantograma é uma frase em que são usadas todas as letras do alfabeto de determinada língua.')
    else:
        print('Não é PANGRAMA.')
        print('Pangrama, ou pantograma é uma frase em que são usadas todas as letras do alfabeto de determinada língua.')

if __name__ == '__main__':

    frase = input('Digite uma frase: ')
    check_alphabet(frase)

#funcionando SAS