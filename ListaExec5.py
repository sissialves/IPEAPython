"""
IPEA - Mestrado em Políticas Públicas e Desenvolvimento
3a. turma
Prof. Bernardo Furtado

Aluna: Sissi Alves da Silva

1a Lista de Exercícios

5. Escreva um programa que recebe uma letra e identifica se ela é vogal ou consoante.
"""

# verificar se a letra digitada minuscula nao existe na nossa variavel vogais

# a função abaixo testa se a letra digitada está na string de vogais,
# em caso afirmativo retorna TRUE, caso contrário retorna false

def test_vogal(l):
        vogais = "aeiou"
        if letra.lower() not in vogais:
            return False
        else:
            return True

if __name__ == '__main__':
    letra = input("Digite uma letra: ")
    print("Você digitou:", letra)

    if test_vogal(letra) == True:
        print("A letra que você digitou é vogal.")
    else:
        print("A letra que você digitou é uma consoante.")

#funcionando SAS