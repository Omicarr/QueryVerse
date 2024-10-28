# QueryVerse

QueryVerse is a powerful tool that converts natural language queries into SQL statements, allowing users to interact with a SQLite database using simple, intuitive language. The project leverages Google's Gemini model to generate SQL queries from user input and displays the results using a Streamlit web application.

## Features

- **Natural Language to SQL Conversion**: Easily convert natural language questions into SQL queries.
- **Streamlit Interface**: User-friendly web interface for inputting queries and viewing results.
- **Google Gemini Integration**: Utilizes Google's Generative AI for accurate SQL query generation.
- **SQLite Database**: Interacts with a pre-defined SQLite database containing various tables related to a bike store.

## Prerequisites

- Python 3.x
- Virtual environment (recommended)
- SQLite
- Google API Key for Gemini model

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/QueryVerse.git
   cd QueryVerse
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your Google API Key:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

## Usage

1. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

2. **Interact with the App**:
   - Open the provided URL in your browser.
   - Enter a natural language query in the input box.
   - Click the "Ask the question" button to generate and execute the SQL query.
   - View the results directly in the app.

## Testing

To run the test suite, execute the following command:

```bash
python -m unittest -v test.py
```

This will run all the test cases and display detailed results.

## Project Structure

- `app.py`: Main application file for the Streamlit interface.
- `sql.py`: Contains functions for database operations.
- `test.py`: Unit tests for the natural language to SQL conversion functionality.
- `requirements.txt`: List of Python dependencies.
- `.env`: Environment variables file (not included in the repository).

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
