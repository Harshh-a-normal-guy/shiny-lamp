import pandas as pd
def csv_to_inputs(csv_path): # if we need csv file for input
    df= pd.read_csv(csv_path)
    input_values=pd.read_csv('Untitled spreadsheet - Sheet1.csv').columns.to_list()


def map_values_to_keys(input_values):
    mapping_rules = {
        'Email': lambda x: 'email' if '@' in x and '.com' in x else None,
        'Username': lambda x: 'username' if x.isalpha() else None,
        'Mobile Number': lambda x: 'mobile_number' if x.isdigit() and len(x) == 10 else None,
        # 'country': lambda x: 'country' if x.isalpha() else None,
    }

    result_dict = {}

    for value in input_values:
        for key, rule_func in mapping_rules.items():
            if (mapped_key := rule_func(value)) is not None:
                result_dict[key] = value
                break
        else:
            # If none of the rules match, set the key to None
            result_dict[value] = None

    return result_dict

# Example usage:
input_values = ['john.doe@example.com', '1234567890', 'JohnDoe']
result = map_values_to_keys(input_values)
print(result)
