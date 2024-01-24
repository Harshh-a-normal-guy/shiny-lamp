from bs4 import BeautifulSoup as bs
from user_data_generated import map_values_to_keys
import pandas as pd
import re
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

