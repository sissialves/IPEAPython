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
    def __init__(self, nId_a):
        self.id = nId_a
        self.balance = 0

    def credit(self, value):
        self.balance += value

    def check_balance(self, amount):
        if self.balance - amount < 0:
            return False
        else:
            return True

    def debit(self, amount):
        self.balance -= amount
        return amount


class Shop:
    def __init__(self, nId_s, i):
        # i é o número de registro
        self.id = nId_s
        self.account = Account(i)
        self.capacity = random.randrange(1, 10)
        self.fun = random.randrange(1, 10)
        self.cost = random.randrange(1, 10)

    def visit(self):
        self.capacity -= 1


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

    def get_fun(self, amount):
        self.fun += amount

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