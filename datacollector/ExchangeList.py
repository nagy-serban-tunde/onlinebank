import time
import math


"""This script defines those lists where 1EURO->?RON, 1EURO->?GBP etc."""

class ExchangeList(object):

    def __init__(self,List_elements):
        self.List_elements = List_elements
        self.List_RONtoEURO_GBP_USD = []
        self.List_EUROtoRON_GBP_USD = []
        self.List_GBPtoRON_EURO_USD = []
        self.List_USDtoRON_EURO_GBP = []

    def RONtoEURO_GBP_USD(self):
        value_pur = 0
        value_sale = 0
        for element in self.List_elements:
            if float(element[2]) != 0 or float(element[3]) != 0:
                value_pur = str(1/float(element[2]))
                value_sale = str(1/float(element[3]))
                self.List_RONtoEURO_GBP_USD += [['RON',element[1],value_pur[:5],value_sale[:5]]]
            else:
                pass

    def EUROtoRON_GBP_USD(self):
        value_pur = 0
        value_sale = 0
        index = 0
        for element in self.List_elements:
            if index %3 == 0:
                euro_pur = self.List_elements[index][2]
                euro_sale = self.List_elements[index][3]
            if element[1] == 'EUR':
                value_pur = element[2]
                value_sale = element[3]
                self.List_EUROtoRON_GBP_USD += [['EUR','RON',value_pur[:5],value_sale[:5]]]
            else:
                if float(element[2]) != 0 or float(element[3]) != 0:
                    value_pur = str((1/float(element[2]))*float(euro_pur))
                    value_sale =str((1/float(element[3]))*float(euro_sale))
                    self.List_EUROtoRON_GBP_USD += [['EUR',element[1],value_pur[:5],value_sale[:5]]]
                else:
                    pass
            index += 1

    def GBPtoRON_EURO_USD(self):
        value_pur = 0
        value_sale = 0
        index = 2
        for element in self.List_elements:
            if index == 2 or index == 5 or index == 8:
                gbp_pur = self.List_elements[index][2]
                gbp_sale = self.List_elements[index][3]
            if element[1] == 'GBP':
                value_pur = element[2]
                value_sale = element[3]
                self.List_GBPtoRON_EURO_USD += [['GBP','RON',value_pur[:5],value_sale[:5]]]
            else:
                if float(element[2]) != 0 or float(element[3]) != 0:
                    value_pur = str((1/float(element[2]))*float(gbp_pur))
                    value_sale =str((1/float(element[3]))*float(gbp_sale))
                    self.List_GBPtoRON_EURO_USD += [['GBP',element[1],value_pur[:5],value_sale[:5]]]
                else:
                    pass
            index += 1
            
    def USDtoRON_EURO_GBP(self):
        value_pur = 0
        value_sale = 0
        index = 1
        for element in self.List_elements:
            if index == 1 or index == 4 or index == 7:
                usd_pur = self.List_elements[index][2]
                usd_sale = self.List_elements[index][3]
            if element[1] == 'USD':
                value_pur = element[2]
                value_sale = (element[3])
                self.List_USDtoRON_EURO_GBP += [['USD','RON',value_pur[:5],value_sale[:5]]]
            else:
                if float(element[2]) != 0 or float(element[3]) != 0:
                    value_pur = str((1/float(element[2]))*float(usd_pur))
                    value_sale =str((1/float(element[3]))*float(usd_sale))
                    self.List_USDtoRON_EURO_GBP += [['USD',element[1],value_pur[:5],value_sale[:5]]]
                else:
                    pass
            index += 1

    def main(self):
        self.RONtoEURO_GBP_USD()
        self.EUROtoRON_GBP_USD()
        self.GBPtoRON_EURO_USD()
        self.USDtoRON_EURO_GBP()
        return( self.List_RONtoEURO_GBP_USD,
                self.List_EUROtoRON_GBP_USD,
                self.List_GBPtoRON_EURO_USD,
                self.List_USDtoRON_EURO_GBP)
