from flask import Flask, render_template, request
import os

app = Flask(__name__)

def generate_custom_html(username, email):
    try:
        # Process the data and generate HTML
        user_data = {'username': username, 'email': email}
        html_data = render_template('user_template.html', user=user_data)

        with open('custom.html', 'w', encoding='utf-8') as file:
            file.write(html_data)
        print('custom.html generated successfully!')
    except Exception as e:
        print(f'Error generating custom.html: {e}')

@app.route('/')
def user_form():
    return render_template('user_form.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    try:
        username = request.form['username']
        email = request.form['email']

        # Process the form data and generate custom HTML
        generate_custom_html(username, email)

        return render_template('success.html', username=username, email=email)
    except Exception as e:
        print(f'Error processing form: {e}')
        return render_template('error.html')

if __name__ == '__main__':
    # Ensure the 'static' folder exists for storing custom.html
    if not os.path.exists('static'):
        os.makedirs('static')
    
    app.run(debug=True)
