from Exex2_Main import Account
from Exex2_Main import Agent
from Exex2_Main import Shop

import random
#função que cria as listas de agentes e das lojas, a partir de um número n e controla
# o id específico. Retorna as listas.
def create(func, n):
    result = list()
    for i in range(n):
        result.append(func(i, i))
    return result
#Método que acessa as contas dos agentes por meio da lista de agentes
# e deposita recursos de forma aleatória, dentro do intervalo abaixo.
def salaries(lst_ag):
    for i in range(len(lst_ag)):
        lst_ag[i].account.credit(random.randrange(10,50))
#Para todos os agentes(lista) escolhe-se uma loja aleatória(actual_shop)
#verifica-se a capacidade da loja, os recursos do agente, visita-se a loja
# computa-se o gasto e adquire-se satisfação.
def interactions(lst_ag, lst_shop):
    for a in lst_ag:
        actual_shop = random.choice(lst_shop)
        if actual_shop.check_capacity() is True:
            if a.check_funds(actual_shop) is True:
                save_shop_cost = actual_shop.cost
                a.account.debit(save_shop_cost)
                actual_shop.account.credit(save_shop_cost)
                a.get_fun(actual_shop.fun)
                actual_shop.visit()

#Método que recebe uma quantidade de agentes e lojas, cria as listas de agentes, mistura os agentes
# cria a lista de lojas, deposita recursos nas contas dos agentes criados
#com os agentes e lojas criados, chama a função de interação.
#Retorna agentes e lojas, após a interação.
def do_interaction(num_agents, num_shops):
    # tipo = Agent()
    agents = create(Agent, num_agents)
    random.shuffle(agents)
    shops = create(Shop, num_shops)
    random.shuffle(shops)
    salaries(agents)
    interactions(agents, shops)
    return agents, shops

#Método que recebe a lista de agentes e calcula a média de satisfação.
def average_fun(lst_ag):
    #for i in range(len(lst_ag)):
     #   print(lst_ag[i].fun)
    soma_fun = sum(lst_ag[i].fun for i in range (len(lst_ag)))
    avg_fun = soma_fun/len(lst_ag)
    return avg_fun
#Método que recebe a lista de lojas e calcula a média do balanço do agentes,
# das lojas e total.
def average_balance(lst_ag, lst_shops):
    soma_balance_ag = sum(lst_ag[i].account.balance for i in range (len(lst_ag)))
    avg_balance_ag = soma_balance_ag/len(lst_ag)
    soma_balance_shops = sum(lst_shops[i].account.balance for i in range(len(lst_shops)))
    avg_balance_shops = soma_balance_shops / len(lst_shops)
    avg_balance = (soma_balance_ag+soma_balance_shops)/(len(lst_ag)+len(lst_shops))
    return avg_balance_ag, avg_balance_shops, avg_balance
#Método que recebe a lista de lojas e calcula a média do custo.
def average_cost(lst_shops):
    #for i in range(len(lst_shops)):
    #   print(lst_shops[i].cost)
    soma_cost = sum(lst_shops[i].cost for i in range (len(lst_shops)))
    avg_cost = soma_cost/len(lst_shops)
    return avg_cost

if __name__ == '__main__':

    #Cria uma lista de agentes e lojas
    agentes, lojas = do_interaction(10,10)

    avg_fun = average_fun(agentes)

    avg_balance_agentes, avg_balance_shops, avg_balance_total = average_balance(agentes, lojas)

    #print(average_cost(lojas))


    #print(avg_balance_agentes, avg_balance_shops, avg_balance_total)

