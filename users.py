# html_generator.py
from flask import render_template,Flask
from user_data_generated import user_data
import pdfkit

app = Flask(__name__)

def generate_html():
    with app.app_context():
        html_data = render_template('user_template.html', user=user_data)
        with open('custom.html', 'w', encoding='utf-8') as file:
            file.write(html_data)

# spark_script.py
# from html_generator import generate_html


# Generate HTML
generate_html()

try:
    # Convert HTML to PDF
    pdfkit.from_file('custom.html', 'custom.pdf')
    print('PDF generated successfully!')
except Exception as e:
    print(f'Error generating PDF: {e}')
