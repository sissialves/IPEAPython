import random
from math import sqrt

params = {'percentual1': .50}


class Firms:

    def __init__(self, name, tipo, preco, capacidade, producao, listacts):
                 #ct1, ct2, ct3, ct4, ct5, ct6):t
        self.name = name
        self.type = tipo
        self.preco = preco
        self.capacidade = capacidade
        self.producao = producao
        self.custo=[]
        for i in range(len(listacts)):
            self.custo.append(listacts[i])

    def calculate_price(self, market):
        ct = 0
        subtotal = 0
        total = list()
        if market.local == "M1":
            ct = self.custo[0]
        elif market.local == "M2":
            ct = self.custo[1]
        elif market.local == "M3":
            ct = self.custo[2]
        elif market.local == "M4":
            ct = self.custo[3]
        elif market.local == "M5":
            ct = self.custo[4]
        elif market.local == 'M6':
            ct = self.custo[5]
        elif market.local == "M7":
            ct = self.custo[6]
        elif market.local == "M8":
            ct = self.custo[7]
        elif market.local == "M9":
            ct = self.custo[8]
        elif market.local == "M10":
            ct = self.custo[9]
        elif market.local == "M11":
            ct = self.custo[10]
        elif market.local == 'M12':
            ct = self.custo[11]
        elif market.local == "M13":
            ct = self.custo[12]
        elif market.local == "M14":
            ct = self.custo[13]
        elif market.local == 'M15':
            ct = self.custo[14]

        for ref in range(len(self.custo)):
            if self.type == 1:
                subtotal = (self.preco*market.volbuy)*(1+market.tax)
            else:
                subtotal = (self.preco*market.volbuy)


        total = subtotal + ct

        return subtotal, ct, total



class Markets:

    def __init__(self, local, demanda, taxa, tipo):
        self.local = local
        self.tax = taxa
        self.demanda = demanda
        self.volume = random.randrange(500, 30000)
        self.volbuy = self.demanda - self.volume
        self.type = tipo

    def decision_buy(self):
        if self.volbuy > (self.demanda * params['percentual1']):
            return True
        else:
            return False

    def get_combustible(self, firm):
        self.volume += self.volbuy
        firm.producao -= self.volbuy
        self.type = firm.type


    def choose_firm(self, mtotal):
        chosen = random.sample(list(mtotal), k=3)
        chosen = {k: mtotal[k] for k in chosen}
        chosen_agent = min(chosen, key=chosen.get)
        return chosen_agent, chosen[chosen_agent]


if __name__ == '__main__':

    pass
