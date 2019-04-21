"""
IPEA - Mestrado em Políticas Públicas e Desenvolvimento
3a. turma
Prof. Bernardo Furtado

Aluna: Sissi Alves da Silva

1a Lista de Exercícios
2. Escreva um programa que imprima o seguinte padrão.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
3. Altere o programa acima para que o usuário possa entrar com o número máximo de estrelas.
"""


def desenho1(l):

    for i in range(1, l+1):
        for j in range(1,i+1):
            print('*', end=' ')
        print('')

    for i in range(-l, -1, 1):
        for j in range(i-1, -2, 1):
            print('*', end=' ')
        print('')

if __name__ == '__main__':

    limite = 5

    desenho1(limite)

    exit(0)

#funcionando SAS