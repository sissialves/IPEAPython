import pandas as pd
from math import sqrt
from Agentes import Firms
from Agentes import Markets
import os


import random

#Função que cria as firmas e os mercados
def create_agents(file_firmas, file_markets):
    data = pd.read_csv(file_firmas, sep=";")
    lst_firmas = []
    for i in range(len(data)):
        lst_firmas.append(Firms(data.loc[i, 'firma'], data.loc[i,'tipo'], data.loc[i, 'preco'], data.loc[i,'capacidade'],
                             data.loc[i,'producao'], [data.loc[i,'ct1'], data.loc[i, 'ct2'], data.loc[i,'ct3'],
                                                      data.loc[i, 'ct4'],
                             data.loc[i,'ct5'], data.loc[i,'ct6'], data.loc[i,'ct7'], data.loc[i,'ct8'], data.loc[i,'ct9'], data.loc[i,'ct10'],
                                                      data.loc[i, 'ct11'], data.loc[i, 'ct12'], data.loc[i,'ct13'], data.loc[i,'ct14'],
                                                      data.loc[i,'ct15']]
                                ))

    data2 = pd.read_csv(file_markets, sep=";")
    lst_markets = []
    for i in range(len(data2)):
        lst_markets.append(Markets(data2.loc[i, 'mercado'], data2.loc[i, 'demanda'], data2.loc[i, 'taxa'],  data2.loc[i, 'tipo']))

    return(lst_firmas, lst_markets)

#Recebe as listas de firmas, realiza a interação: a compra de combustível mais barato
def do_interaction(lst_firmas, lst_markets):
    if os.path.exists(file):
        os.remove(file)
    with open(file, 'a') as f:
        f.write('\n')
        f.write(
            'Mercado; Firma Escolhida; Gasto; Volume Comprado\n');

        mtotal = {}
        for m in lst_markets:
            if m.decision_buy()== True:
                for ref in lst_firmas:
                    subtotal, ct, total = ref.calculate_price(m)
                    mtotal[ref] = total
                chosenfirm, gasto = m.choose_firm(mtotal)
                f.write(
                    '{};{};{:.2f};{:.2f}\n'.format(m.local, chosenfirm.name, gasto, m.volbuy))
                f.write('')

    return 0
if __name__ == '__main__':


    file_firmas = 'Firmas.csv'
    file_markets = 'Markets.csv'
    file = "Results.csv"



    lst_firmas, lst_markets =create_agents(file_firmas, file_markets)

    do_interaction(lst_firmas, lst_markets)

