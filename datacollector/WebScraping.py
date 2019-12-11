import bs4 as bs 
from urllib.request import Request, urlopen

"""This script is responsible for downloading the webpage content"""

class WebScraping(object):

    def __init__(self):
        self.webpages = []
        self.webpages_name = []
        self.List_elements = []

    def webpages_load (self):
        req1 = Request('https://www.otpbank.ro/hu/valutarfolyam', headers={'User-Agent': 'Google Chrome'})
        self.webpages_name += ['https://www.otpbank.ro/hu/valutarfolyam']
        self.webpages += [req1]
        req2 = Request('http://www.lillapanzio.ro/valutavalto', headers={'User-Agent': 'Google Chrome'})
        self.webpages_name += ['http://www.lillapanzio.ro/valutavalto']
        self.webpages += [req2]
        req3 = Request('https://www.curs-valutar-bnr.ro/curs-valutar-banci/unicredit-tiriac-bank', headers={'User-Agent': 'Google Chrome'})
        self.webpages_name += ['https://www.curs-valutar-bnr.ro/curs-valutar-banci/unicredit-tiriac-bank']
        self.webpages += [req3]
    
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
    
    def main(self):
        self.webpages_load()
        self.search_table()
        return (self.webpages,
                self.webpages_name,
                self.List_elements)
