<!-- # Data Mapper

This Python script (`users.py`) is designed to generate custom HTML  and PDf file based on user data. It utilizes Flask to render an HTML template (`user_template.html`) with dynamically generated user data.

## Usage

1. Make sure you have Python and Flask installed in your environment.Use requirements.txt to install dependencies.

2. Run the script by executing the following command in your terminal:

    ```bash
    python users.py
    ```

3. The script will generate an HTML file named `custom.html` in the same directory.

## Dependencies

- Flask: The script uses Flask to create an application context for rendering the HTML template.

## Files

- `users.py`: The main script that generates the HTML and pdf file.
- `user_template.html`: The HTML template that includes placeholders for user data.
- `user_data_generated.py`: Contains sample user data used in the template.

## License

This project is licensed under the [MIT License](LICENSE). -->
# Data Mapper

This Python script (`users.py`) is designed to generate a PDF of a web form based on user data collected from three different sources. The script combines information from these sources and creates a comprehensive PDF report.

## Usage

1. **Install Dependencies:** Ensure you have the required dependencies installed. You can use the following command to install them:

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Script:** Execute the script by running the following command in your terminal:

    ```bash
    python data_mapper.py
    ```

3. **Generate PDF:** The script will fetch data from three different sources, process it, and generate a PDF report named `webform_report.pdf` in the same directory. You have to provide from where you need to generate the data.

## Sources of Data

- **Source 1:** Input from [Source 1 Csv].
- **Source 2:** Input from [Source 2 Webform].
- **Source 3:** Input from [Source 3 Mail].

## Dependencies

- Flask: The script may use Flask to manage certain aspects of data processing.

## Files

- `users.py`: The main script responsible for collecting data from three sources and generating the PDF report.
- `user_template.html`: The HTML template used for creating the PDF report.


## Output

- `custom.pdf`: The final PDF report containing combined data from one of the three  sources.

## License

This project is licensed under the [MIT License](LICENSE).
