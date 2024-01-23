from bs4 import BeautifulSoup as bs
from mail2 import get_body,main,decode_body
from user_data_generated import map_values_to_keys
import pandas as pd
import re
a= main()
soup=bs(a,'lxml')
lst= list(''.join(soup.text))[0:60]
def generate_inputs_from_bs4(lst):
    character_string=''
    input_data_creation=[]
    for char in lst:
        if re.match(r'[a-zA-Z0-9.@]', char):
            character_string+=char
        else:
            if character_string:

                input_data_creation.append(character_string)
                character_string=''
    return input_data_creation

input_data_list_bs4=set(generate_inputs_from_bs4(lst))
print(set(input_data_list_bs4))
print(map_values_to_keys(list(input_data_list_bs4)))
