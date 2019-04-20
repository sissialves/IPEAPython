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

#Função que acrescenta um dadd ao dicionário
def acrescente(d1):
    d1['b'] = 1

    return d1

def test_letra(d2):

    d3 = dict.keys(d2)
    if "c" not in d3:
        return False
    else:
        return True

def concate_dict(d4):
    d5 = {'z': 23}
    d4.update(d5)
    return d4


if __name__ == '__main__':
    meudict1 = dict()
    meudict1['a'] = 0
    print("Meu primeiro dicionário é:",meudict1)

    meudict2 = {}
    meudict2 = acrescente(meudict1)
    print("Meu novo dicionário é:", acrescente(meudict1))

    if test_letra(meudict2) == True:
        print("A letra c consta do dicionário")
    else:
        print("A letra c não consta do dicionário")

    concate_dict(meudict2)
    print("Meu dicionário concatenado é:", meudict2)
    exit(0)
