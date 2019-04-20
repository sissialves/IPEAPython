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
def desenho2(l, num):

    count1 = 0
    count2 = 0

    for i in range(1, l+1):
        for j in range(1,i+1):
            print('*', end=' ')
            count1 = count1 + 1
            if count1 > (num//2):
                break
        print('')

    for i in range(-l+1, -1, 1):
        for j in range(i-1, -2, 1):
            print('*', end=' ')
            count2 = count2 + 1
        print('')
    total = count1+count2

    print(total, count1,count2)

if __name__ == '__main__':

    numestrelas = int(input("Digite o número máximo de estrelas:"))
    limite = 5
    desenho2(limite, numestrelas)

    exit(0)