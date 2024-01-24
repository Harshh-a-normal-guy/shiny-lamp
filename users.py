

import pandas as pd
from flask import render_template, Flask
from user_data_generated import csv_to_inputs,map_values_to_keys
import pdfkit

#html template with custom data
# it is the last step 

app = Flask(__name__)
clash_keywords= ['WiseStamp','Analyst','Aspiring']
# clash words 


dict=csv_to_inputs('data.csv').to_dict()
users=[]
# print(dict)
for i in range(len(dict['name'].keys())):
    users.append([dict['name'][i],dict['mail'][i]
                ,dict['Mobile'][i]])


def generate_html(users):
    for i, user in enumerate(users,start=1):
        with app.app_context():
            try:
                dict= map_values_to_keys(user)
                # print(dict)
                # Pass the user data explicitly to render_template
                html_data = render_template('user_template.html', user=dict)


            #     # Create a unique filename for each user
                filename = f'custom_{i}.html'
                
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(html_data)
                
                print(f'HTML generated for user {i} successfully!')
                
                # Convert HTML to PDF
                pdfkit.from_file(filename, f'custom_{i}.pdf')
                print(f'PDF generated for user {i} successfully!')
            except Exception as e:
                print(f'Error generating HTML for user {i+1}: {e}')

print(generate_html(users))







