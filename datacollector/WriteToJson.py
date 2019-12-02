import json


def json_file_upload(file, json_list,webpages_name):
    list = []
    index = 0
    for i in range(len(json_list)):
        if i == 3 or i == 6:
            index += 1
        else:
            pass
        element = {
            'web_address' : webpages_name[index],
            'currency': json_list[i][1],
            'purchase_price':json_list[i][2],
            'sale_price': json_list[i][3]
        }
        list += [element]
    with open(file,'w') as json_file:
         json.dump(list,json_file)
    list.clear()
