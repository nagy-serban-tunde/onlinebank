from WebScraping import WebScraping
from DataCleaning import DataCleaning
from ExchangeList import ExchangeList
from BestExchangeValuta import BestExchangeValuta
from ValutaMySqlLoading import ValutaMySqlLoading
from TablesCreated import TablesCreated
import WriteToJson

    
if __name__ == "__main__":
    obj = WebScraping()
    obj.search_table()
    webpages, webpages_name, List_elements = obj.main()

    List_elements = DataCleaning(List_elements).main()
    # WriteToJson.json_file_upload('..\\frontend\\static\\WebScraping.json',List_elements,webpages_name)

    List_RONtoEURO_GBP_USD,List_EUROtoRON_GBP_USD,List_GBPtoRON_EURO_USD,List_USDtoRON_EURO_GBP = ExchangeList(List_elements).main()
    # WriteToJson.json_file_upload('..\\frontend\\static\\RON.json',List_RONtoEURO_GBP_USD,webpages_name)
    # WriteToJson.json_file_upload('..\\frontend\\static\\EUR.json',List_EUROtoRON_GBP_USD,webpages_name)
    # WriteToJson.json_file_upload('..\\frontend\\static\\GBP.json',List_GBPtoRON_EURO_USD,webpages_name)
    # WriteToJson.json_file_upload('..\\frontend\\static\\USD.json',List_USDtoRON_EURO_GBP,webpages_name)

    TablesCreated("online_bank","127.0.0.1","root","diak123").main()

    ListBestExchangeValutaRON = BestExchangeValuta(webpages_name,List_RONtoEURO_GBP_USD,['EUR','GBP','USD']).main()
    ValutaMySqlLoading(ListBestExchangeValutaRON,"RON","online_bank","127.0.0.1","root","diak123").main()

    ListBestExchangeValutaEUR = BestExchangeValuta(webpages_name,List_EUROtoRON_GBP_USD,['RON','GBP','USD']).main()
    ValutaMySqlLoading(ListBestExchangeValutaEUR,"EUR","online_bank","127.0.0.1","root","diak123").main()

    ListBestExchangeValutaGBP = BestExchangeValuta(webpages_name,List_GBPtoRON_EURO_USD,['RON','EUR','USD']).main()
    ValutaMySqlLoading(ListBestExchangeValutaGBP,"GBP","online_bank","127.0.0.1","root","diak123").main()

    ListBestExchangeValutaUSD = BestExchangeValuta(webpages_name,List_USDtoRON_EURO_GBP,['RON','EUR','GBP']).main()
    ValutaMySqlLoading(ListBestExchangeValutaUSD,"USD","online_bank","127.0.0.1","root","diak123").main()

    
