import math

class BestExchangeValuta(object):

    def __init__(self, webpages_name, lista, valuta):
        self.lista = lista
        self.valuta = valuta
        self.webpages_name = webpages_name
        self.List_BestExchangeValuta = []

    def the_best_search_valuta(self, valuta):
            temp = []
            minimum = (math.inf,0)
            for i in range(len(self.lista)):
                if(self.lista[i][2] == valuta):
                    temp+=[self.lista[i]]
            for i in range(len(temp)):
                if minimum[0] > float(temp[i][3]):
                    minimum = (float(temp[i][3]),i)
            self.List_BestExchangeValuta += [temp[minimum[1]]]
            
    def main(self):
        index = 0
        for i in range(len(self.lista)):
            if i == 3 or i == 6:
                index += 1
            self.lista[i] = [self.webpages_name[index]] + self.lista[i]

        for i in range(len(self.valuta)):
            self.the_best_search_valuta(self.valuta[i])  

        return self.List_BestExchangeValuta