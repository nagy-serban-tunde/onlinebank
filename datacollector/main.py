from WebScraping import WebScraping
from DataCleaning import DataCleaning
from ExchangeList import ExchangeList
from BestExchangeValuta import BestExchangeValuta
import WriteToJson

    
if __name__ == "__main__":
    obj = WebScraping()
    obj.search_table()
    webpages, webpages_name, List_elements = obj.main()

    obj = DataCleaning(List_elements)
    List_elements = obj.main()

    WriteToJson.json_file_upload('..\\frontend\\static\\WebScraping.json',List_elements,webpages_name)

    List_RONtoEURO_GBP_USD,List_EUROtoRON_GBP_USD,List_GBPtoRON_EURO_USD,List_USDtoRON_EURO_GBP = ExchangeList(List_elements).main()
    # WriteToJson.json_file_upload('..\\frontend\\static\\RON.json',List_RONtoEURO_GBP_USD,webpages_name)
    # WriteToJson.json_file_upload('..\\frontend\\static\\EUR.json',List_EUROtoRON_GBP_USD,webpages_name)
    # WriteToJson.json_file_upload('..\\frontend\\static\\GBP.json',List_GBPtoRON_EURO_USD,webpages_name)
    # WriteToJson.json_file_upload('..\\frontend\\static\\USD.json',List_USDtoRON_EURO_GBP,webpages_name)

    ListBestExchangeValutaRON = BestExchangeValuta(webpages_name,List_RONtoEURO_GBP_USD,['EUR','GBP','USD']).main()
    print(ListBestExchangeValutaRON)
    ListBestExchangeValutaEUR = BestExchangeValuta(webpages_name,List_EUROtoRON_GBP_USD,['RON','GBP','USD']).main()
    print(ListBestExchangeValutaEUR)
    ListBestExchangeValutaGBP = BestExchangeValuta(webpages_name,List_GBPtoRON_EURO_USD,['RON','EUR','USD']).main()
    print(ListBestExchangeValutaGBP)
    ListBestExchangeValutaUSD = BestExchangeValuta(webpages_name,List_USDtoRON_EURO_GBP,['RON','EUR','GBP']).main()
    print(ListBestExchangeValutaUSD)

    
