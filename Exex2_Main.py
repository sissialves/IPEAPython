"""
IPEA
Mestrado Profissional em Políticas Públicas e Desenvolvimento
Disciplina: Python para Metodologia Baseada em Agentes
2a. Lista de Exercícios
Aluna: Sissi Alves da Silva
1. Objetivo: criar agentes e interações. Agentes vão às compras e ganham satisfação. Lojas, com capacidade
limitada recebem os clientes. Vendem satisfação. Análise da interação (simples) na medida em que se aumentam
clientes.
"""

import random


class Account:
    #Toda conta recebe um Id como parâmetro de entrada.
    def __init__(self, nId_a):
        self.id = nId_a
        self.balance = 0
    #Método que recebe recursos amount e acrescenta ao balanço.
    def credit(self, value):
        self.balance += value

    #Verifica se a conta tem os recursos necessários(amount). Retorna True se houver recursos
    #retorna False, caso contrário
    def check_balance(self, amount):
        if self.balance - amount < 0:
            return False
        else:
            return True
    # Método que retira recursos (amount) do balanço e retorna a quantia
    #retirada.
    def debit(self, amount):
        self.balance -= amount
        return amount


class Shop:
    def __init__(self, nId_s, i):
        # i é o número de registro
        self.id = nId_s
        self.account = Account(i)
        # as variáveis capacity, fun e cost são geradas, no momento de criação da
        #instância com valores aleatórios dentro das faixas abaixo:
        self.capacity = random.randrange(100, 105)
        self.fun = random.randrange(4, 8)
        self.cost = random.randrange(20, 30)
    # Método que diminui a capacidade da loja de 1, sempre que ocorrer uma visita
    # de um cliente.
    def visit(self):
        self.capacity -= 1

    #Método que verifica a capacidade da loja.
    # Se a capacidade chegar a zero, retorna False. Senão, retorna True
    def check_capacity(self):
        if self.capacity == 0:
            return False
        else:
            return True

class Agent:
    def __init__(self, nId_ag, i):
        #i é o número de registro
        self.fun = 0
        self.id = nId_ag
        self.account = Account(i)
    #Método que acumula a satisfação do cliente, ao visitar uma loja.
    #Recebe o valor necessário para pagar à loja.
    def get_fun(self, amount):
        self.fun += amount
    #Método que verifica se os recursos do Agent são suficientes para bancar o Shop.cost
    def check_funds(self, shop):
        if self.account.balance > shop.cost:
            return True
        else:
            return False

    # ============================================================================================
    # Função Principal
    # ============================================================================================
if __name__ == '_main_':
    a1 = Agent(0, 0)
    s1 = Shop(1, 1)
    a1.account.deposit(10)
    s1.account.deposit(s1.cost)
    a1.account.pay(s1.cost)
    print('O custo da loja {} é R${:.2f} e a fun é {}.'.format(s1.id, s1.cost, s1.fun))
    print('O balanço corrente da loja {} é R${:.2f}'.format(s1.id, s1.account.balance))
    print('O agente tem R${:.2f} em caixa'.format(a1.account.balance))