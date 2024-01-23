from flask import Flask, render_template, request
import pdfkit

app = Flask(__name__)

# Dictionary to store submitted details
user_data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Retrieve form data
    name = request.form['name']
    mobile = request.form['mobile']
    email = request.form['email']

    # Store data in the dictionary
    user_data = {
        'Username': name,
        'Mobile_Number': mobile,
        'Email': email
    }
    print(user_data)
    html_data=render_template('user_template.html', user=user_data)
    with open('custom.html','w',encoding='utf-8') as file:
        file.write(html_data)
    pdfkit.from_file('custom.html','custom.pdf')

    return render_template('success.html',user=user_data) 
if __name__ == '__main__':
    app.run(debug=True)
