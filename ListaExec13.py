"""
IPEA - Mestrado em Políticas Públicas e Desenvolvimento
3a. turma
Prof. Bernardo Furtado

Aluna: Sissi Alves da Silva

1a Lista de Exercícios

13. Escreva um programa que substitua ‘,’ por ‘.’ e ‘.’ por ‘,’ em uma string. Exemplo: 1,000.54
por 1.000,54.
"""

def substitue_pontuacao(p):

    if "," in p:
        p2 = str.replace(p,',',':')
    if "." in p2:
        p3 = str.replace(p2, ".", ",")
    if ":" in p3:
        p4 = str.replace(p3, ":", ".")

    return p4

if __name__ == '__main__':

    palavra1 = "1,000.54"
    palavra2 = "1.000.540,00"

    print('Exemplo 1: A string inicial: ', palavra1)
    print('A nova palavra é: ', substitue_pontuacao(palavra1))

    print('Exemplo 2: A string inicial: ', palavra2)
    print('A nova palavra é: ', substitue_pontuacao(palavra2))
    exit(0)
#funcionando! SAS