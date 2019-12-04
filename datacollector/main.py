from WebScraping import WebScraping
from DataCleaning import DataCleaning
from ExchangeList import ExchangeList
from BestExchangeValuta import BestExchangeValuta
from ValutaMySqlLoading import ValutaMySqlLoading
from TablesCreated import TablesCreated
import insert_table

    
if __name__ == "__main__":
    webpages, webpages_name, List_elements = WebScraping().main()

    List_elements = DataCleaning(List_elements).main()

    List_RONtoEURO_GBP_USD,List_EUROtoRON_GBP_USD,List_GBPtoRON_EURO_USD,List_USDtoRON_EURO_GBP = ExchangeList(List_elements).main()

    # TablesCreated("online_bank","127.0.0.1","root","diak123").main()
    # insert_table.InsertToTable()

    ValutaMySqlLoading(List_elements,"Valuta","online_bank","127.0.0.1","root","diak123").ValutaTableUpload(webpages_name)

    ListBestExchangeValutaRON = BestExchangeValuta(webpages_name,List_RONtoEURO_GBP_USD,['EUR','GBP','USD']).main()
    ValutaMySqlLoading(ListBestExchangeValutaRON,"RON","online_bank","127.0.0.1","root","diak123").Insert_Update_Element_In_Table()

    ListBestExchangeValutaEUR = BestExchangeValuta(webpages_name,List_EUROtoRON_GBP_USD,['RON','GBP','USD']).main()
    ValutaMySqlLoading(ListBestExchangeValutaEUR,"EUR","online_bank","127.0.0.1","root","diak123").Insert_Update_Element_In_Table()

    ListBestExchangeValutaGBP = BestExchangeValuta(webpages_name,List_GBPtoRON_EURO_USD,['RON','EUR','USD']).main()
    ValutaMySqlLoading(ListBestExchangeValutaGBP,"GBP","online_bank","127.0.0.1","root","diak123").Insert_Update_Element_In_Table()

    ListBestExchangeValutaUSD = BestExchangeValuta(webpages_name,List_USDtoRON_EURO_GBP,['RON','EUR','GBP']).main()
    ValutaMySqlLoading(ListBestExchangeValutaUSD,"USD","online_bank","127.0.0.1","root","diak123").Insert_Update_Element_In_Table()

    
