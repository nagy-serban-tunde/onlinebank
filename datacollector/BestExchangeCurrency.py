import math

"""This script decides that which webpage offers the best exhange rate"""

class BestExchangeCurrency(object):

    def __init__(self, webpages_name, lista, currency):
        self.lista = lista
        self.currency = currency
        self.webpages_name = webpages_name
        self.List_BestExchangeCurrency = []

    def the_best_search_currency(self, currency):
            temp = []
            minimum = (math.inf,0)
            for i in range(len(self.lista)):
                if(self.lista[i][2] == currency):
                    temp+=[self.lista[i]]
            for i in range(len(temp)):
                if minimum[0] > float(temp[i][3]):
                    minimum = (float(temp[i][3]),i)
            self.List_BestExchangeCurrency += [temp[minimum[1]]]
            
    def main(self):
        index = 0
        for i in range(len(self.lista)):
            if i == 3 or i == 6:
                index += 1
            self.lista[i] = [self.webpages_name[index]] + self.lista[i]

        for i in range(len(self.currency)):
            self.the_best_search_currency(self.currency[i])  

        return self.List_BestExchangeCurrency