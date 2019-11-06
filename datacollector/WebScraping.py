import bs4 as bs
import re
import json
import time
from urllib.request import Request, urlopen

class WebScraping(object):

    def __init__(self, webpages, webpages_name):
        self.webpages = webpages
        self.webpages_name = webpages_name
        self.List_elements = []
        self.List_EUROtoRON_GBP_USD = []
        self.List_GBPtoRON_EURO_USD = []
        self.List_USDtoRON_EURO_GBP = []
        self.WebScrapingMain()
    
    #a weboldalakon keresi a tablazatokat
    def search_table(self):
        for i in self.webpages:
            source = urlopen(i).read()
            soup = bs.BeautifulSoup(source,'lxml')
            table = soup.find('table')
            table_rows = table.find_all('tr')
            for tr in table_rows:
                td = tr.find_all('td')
                row = [i.text for i in td]
                self.List_elements += [row]

    # megtisztitja a felesleges listaktol mint pl az ures lista
    def redundant_list_removal(self,list):
        temp_list = []
        for i in range(len(list)):
            if list[i] != '':
                temp_list += [list[i]]
            else:
                pass
        return temp_list

    #valuta kivalasztas
    def currency_choosing(self, list, temp_List_elements):
        for element in list:
            if element == 'USD' or element == 'GBP' or element == 'EUR':
                temp_List_elements.append(list)
            else:
                pass
    
    # megfelelo hosszusagu lesz a lista
    def list_cut(self,list):
        temp = []
        if len(list)>3:
            for i in range(len(list)):
                if i != 1:
                    temp += [list[i]]
                else:
                    pass
            return temp
        else:
            return list

    #levagja a listak vegerol a RON szot
    def list_end_cut_RON(self,list):
        for i in range(len(list)):
            if list[i][(len(list[i])-3):] == 'RON':
                list[i]=list[i][:(len(list[i])-3)]
            else:
                pass
        return (list)

    #neki fog tisztitani a bejovo adatot
    def data_cleaning(self):
        temp_List_elements = []
        for data in self.List_elements:
            if data != []:
                temp = ''
                for element in data:
                    element = re.sub('\t','',element)
                    element = re.sub('\n','',element)
                    element = re.sub('\r','',element)
                    element = re.sub(' ','',element)
                    element = re.sub(',','.',element)
                    temp += element
                    temp += ' '
                temp = temp.split(' ')
                temp = self.redundant_list_removal(temp)
                self.currency_choosing(temp,temp_List_elements)
            else:
                pass
        self.List_elements = []
        for element in temp_List_elements:
            element = self.list_cut(element)
            element = self.list_end_cut_RON(element)
            element = ['RON'] + element
            self.List_elements += [element]
        temp_List_elements.clear()

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
                value_pur = str((1/float(element[2]))*float(euro_pur))
                value_sale =str((1/float(element[3]))*float(euro_sale))
                self.List_EUROtoRON_GBP_USD += [['EUR',element[1],value_pur[:5],value_sale[:5]]]
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
                value_pur = str((1/float(element[2]))*float(gbp_pur))
                value_sale =str((1/float(element[3]))*float(gbp_sale))
                self.List_GBPtoRON_EURO_USD += [['GBP',element[1],value_pur[:5],value_sale[:5]]]
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
                value_pur = str((1/float(element[2]))*float(usd_pur))
                value_sale =str((1/float(element[3]))*float(usd_sale))
                self.List_USDtoRON_EURO_GBP += [['USD',element[1],value_pur[:5],value_sale[:5]]]
            index += 1

    def json_file_upload(self,file, json_list):
        list = []
        index = 0
        for i in range(len(json_list)):
            if i == 3 or i == 6:
                index += 1
            else:
                pass
            element = {
                'web_address' : self.webpages_name[index],
                'currency': json_list[i][1],
                'purchase_price':json_list[i][2],
                'sale_price': json_list[i][3]
            }
            list += [element]
        with open(file,'w') as json_file:
             json.dump(list,json_file)
        list.clear()
        
    def WebScrapingMain(self):
        self.search_table()
        self.data_cleaning()
        self.EUROtoRON_GBP_USD()
        self.json_file_upload('..\\frontend\\static\\EURO.json',self.List_EUROtoRON_GBP_USD)
        self.GBPtoRON_EURO_USD()
        self.json_file_upload('..\\frontend\\static\\GBP.json',self.List_GBPtoRON_EURO_USD)
        self.USDtoRON_EURO_GBP()
        self.json_file_upload('..\\frontend\\static\\USD.json',self.List_USDtoRON_EURO_GBP)
        self.List_elements.clear()
        self.List_EUROtoRON_GBP_USD.clear()
        self.List_GBPtoRON_EURO_USD.clear()
        self.List_USDtoRON_EURO_GBP.clear()

if __name__ == "__main__":
    webpages = []
    webpages_name = []
    req1 = Request('https://www.otpbank.ro/hu/valutarfolyam', headers={'User-Agent': 'Google Chrome'})
    webpages_name += ['https://www.otpbank.ro/hu/valutarfolyam']
    webpages += [req1]
    req2 = Request('http://www.lillapanzio.ro/valutavalto', headers={'User-Agent': 'Google Chrome'})
    webpages_name += ['http://www.lillapanzio.ro/valutavalto']
    webpages += [req2]
    req3 = Request('https://www.curs-valutar-bnr.ro/curs-valutar-banci/unicredit-tiriac-bank', headers={'User-Agent': 'Google Chrome'})
    webpages_name += ['https://www.curs-valutar-bnr.ro/curs-valutar-banci/unicredit-tiriac-bank']
    webpages += [req3]
    # while 1:
    #     obj = WebScraping(webpages,webpages_name)
    #     del(obj)
    #     time.sleep(0.1)
    obj = WebScraping(webpages,webpages_name)
    del(obj)
        