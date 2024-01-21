
# from flask import render_template,Flask
# from user_data_generated import result
# import pdfkit

# app = Flask(__name__)

# def generate_html():
#     with app.app_context():
#         html_data = render_template('user_template.html', user=result)
#         with open('custom.html', 'w', encoding='utf-8') as file:
#             file.write(html_data)


# # Generate HTML
# generate_html()

# try:
#     # Convert HTML to PDF
#     pdfkit.from_file('custom.html', 'custom.pdf')
#     print('PDF generated successfully!')
# except Exception as e:
#     print(f'Error generating PDF: {e}')
from flask import render_template, Flask
from user_data_generated import result
import pdfkit

app = Flask(__name__)

def generate_html():
    with app.app_context():
        try:
            # Pass the user data explicitly to render_template
            html_data = render_template('user_template.html', user=result)
            with open('custom.html', 'w', encoding='utf-8') as file:
                file.write(html_data)
            print('HTML generated successfully!')
        except Exception as e:
            print(f'Error generating HTML: {e}')

try:
    # Generate HTML
    generate_html()

    # Convert HTML to PDF
    pdfkit.from_file('custom.html', 'custom.pdf')
    print('PDF generated successfully!')
except Exception as e:
    print(f'Error generating PDF: {e}')
