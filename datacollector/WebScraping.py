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
        self.List_valutas  = ['RON','GBP', 'USD']
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

    #  def json_file_upload(self):
    #     list = []
    #     index = 0
    #     for i in range(len(self.List_elements)):
    #         if i == 3 or i == 6:
    #             index += 1
    #         else:
    #             pass
    #         element = {
    #             'web_address' : self.webpages_name[index],
    #             'currency': self.List_elements[i][0],
    #             'purchase_price':self.List_elements[i][1],
    #             'sale_price': self.List_elements[i][2]
    #         }
    #         list += [element]
    #     with open('..\\frontend\static\WebScraping.json','w') as json_file:
    #          json.dump(list,json_file)

    def json_file_upload(self):
        list = []
        list1 = []
        list2 = []
        a=0
        b=3
        for i in range(len(self.webpages_name)):
            list2.clear()
            for j in range(a,b):
                # print (self.List_elements[j][1],self.List_elements[j][2],self.List_elements[j][3])
                element2 = {
                        'currency': self.List_elements[j][1],
                        'purchase_price':self.List_elements[j][2],
                        'sale_price': self.List_elements[j][3]
                }
                list2 += [element2]
            element1 = {
                'web_address' : self.webpages_name[i],
                'values' : list2,
            }
            list1 += [element1]
            print(element1)
            a += 3
            b += 3

        # for i in list1:
        #     print(i)

        for valuta in range(len(self.List_valutas)):
            if self.List_valutas[valuta] == self.List_elements[valuta][0]:
                element = {
                    'from': self.List_valutas[valuta],
                    'web_page':list1
                }
                list += [element]
        with open('..\\frontend\\static\\WebScraping.json','w') as json_file:
             json.dump(list,json_file)
        
    def WebScrapingMain(self):
        self.search_table()
        self.data_cleaning()
        self.json_file_upload()

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
        