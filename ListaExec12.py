"""
IPEA - Mestrado em Políticas Públicas e Desenvolvimento
3a. turma
Prof. Bernardo Furtado

Aluna: Sissi Alves da Silva

1a Lista de Exercícios

12. Escreva uma função que liste todos os números primos até 200. Utilize a divisão modular
(%).
"""
# Função que indica os números primos até o limite definido, nese caso, o limite é 200.

def testeprimo(numero):
    lista_numeros =[]
    divisores =[]

    for i in range(2, numero + 1):
        for j in range(1, i+1):
            if i >= j:
                if i % j == 0:
                    divisores.append(j)
         #se a lista de divisores do número é maior que 2, não é primo.
        if len(divisores) == 2:
            lista_numeros.append(i)
        divisores = []
    return lista_numeros

if __name__ == '__main__':
#limite do loop
    limite = 200
    qtdade = testeprimo(limite)

    print(" Existem {} números primos até 200.".format(len(qtdade)))
    print(" São eles:",qtdade)