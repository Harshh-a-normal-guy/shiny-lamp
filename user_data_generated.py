# maps data according to constraint
import pandas as pd
#for csv to inputs

clash_keywords= ['WiseStamp','Analyst','Aspiring']
def map_values_to_keys(input_values):
    inputs=[]
    for val in input_values:
        if val not in clash_keywords:
            inputs.append(val)

    mapping_rules = {
        'Email': lambda x: "Email" if '@' in x and '.com'  in x else None,
        'Username': lambda x: 'Username' if x.isalpha() and len(x) >= 5 and x[0].isupper() else None
,
        'Mobile Number': lambda x: 'Mobile Number' if x.isdigit() and len(x) == 10 else None,
        # 'country': lambda x: 'country' if x.isalpha() else None,
    }

    result_dict = {}

    for value in inputs:
        for key, rule_func in mapping_rules.items():
            if (mapped_key := rule_func(value)) is not None:
                result_dict[key] = value
                break
        else:
            # If none of the rules match, set the key to None
            # result_dict[value] = None
            pass

    return result_dict




def csv_to_inputs(csv_path): # if we need csv file for input
    df= pd.read_csv(csv_path)
    input_values=pd.read_csv('Untitled spreadsheet - Sheet1.csv').columns.to_list()

# # Example usage:
input_values = ['john.doe@example.com', '1234567890', 'JohnDoe']
result = map_values_to_keys(input_values)
# print(result)
