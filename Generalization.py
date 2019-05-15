from Exex2_Main import Account
from Exex2_Main import Agent
from Exex2_Main import Shop
from Interactions import do_interaction
from Interactions import average_fun
from Interactions import average_balance
from Interactions import average_cost



import random

def create_list(nagents, nshops):
    res1 = list()
    res2 = list()
    for i in range(1,nagents):
        res1.append(i*10)
    for i2 in range(1,nshops):
        res2.append(i2 * 5)
    return res1,res2




if __name__ == '__main__':
    lista_ag, lista_shops=create_list(20, 30)

    #print(lista_ag, lista_shops)

    with open('saida.csv', 'a') as f:
        f.write(
            str([lista_ag, lista_shops]))
        f.write('\n')
        for i in range(len(lista_ag)):


            clientes, lojas = do_interaction(lista_ag[i], lista_shops[i])

            #print(average_cost(lojas), average_balance(clientes,lojas), average_fun(clientes))
            f.write(str([clientes[i], lojas[i], average_fun(clientes), average_balance(clientes, lojas), average_cost(lojas)]))
            f.write('\n')





