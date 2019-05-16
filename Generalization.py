from Exex2_Main import Account
from Exex2_Main import Agent
from Exex2_Main import Shop
from Interactions import do_interaction,average_fun, average_balance, average_cost
import os
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
    file='saida.csv'

    #print(lista_ag, lista_shops)
    if os.path.exists(file):
        os.remove(file)
    with open(file, 'a') as f:
        #f.write(
          #  str([lista_ag, lista_shops]))
        f.write('\n')
        f.write('ID Cliente; ID Loja; Media FUN; Media Balance Agentes; Media Balance Lojas; Media Balance Total; Custo Medio\n');

        for i in range(len(lista_ag)):

            clientes, lojas = do_interaction(lista_ag[i], lista_shops[i])

            md_balance_clientes, md_balance_shops, md_balance_total = average_balance(clientes, lojas)
            #print(average_cost(lojas), average_balance(clientes,lojas), average_fun(clientes))
            f.write('{};{};{:.2f};{:.2f};{:.2f};{:.2f};{:.2f}\n'.format(clientes[i].id, lojas[i].id, average_fun(clientes), md_balance_clientes, md_balance_shops, md_balance_total, average_cost(lojas)))
            f.write('\n')





