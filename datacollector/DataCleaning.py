import re # replaces given character by another character

"""This page is responsible for cleaning the data downloaded by WebScrepper"""
class DataCleaning(object):
    def __init__(self,List_elements):
        self.List_elements = List_elements

    def redundant_list_removal(self,list):
        temp_list = []
        for i in range(len(list)):
            if list[i] != '':
                temp_list += [list[i]]
            else:
                pass
        return temp_list

    def currency_choosing(self, list, temp_List_elements):
        for element in list:
            if element == 'USD' or element == 'GBP' or element == 'EUR':
                temp_List_elements.append(list)
            else:
                pass
    
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

    def list_end_cut_RON(self,list):
        for i in range(len(list)):
            if list[i][(len(list[i])-3):] == 'RON':
                list[i]=list[i][:(len(list[i])-3)]
            else:
                pass
        return (list)

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
    
    def main(self):
        self.data_cleaning()
        return self.List_elements


