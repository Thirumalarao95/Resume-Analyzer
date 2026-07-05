# Resume Analyzer

This project is a resume analyzer that uses AI to extract key information from resumes and provide insights. It leverages the following technologies:

- Python
- Streamlit
- Ollama


## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Thirumalarao95/Resume-Analyzer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Resume-Analyzer
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   .
vend/bin/activate  # On Linux/macOS
   .\venv\Scripts\activate  # On Windows
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Make sure Ollama is running and the necessary models are downloaded.

## Usage

To run the Streamlit application, execute the following command:

```bash
streamlit run app.py
```

## Project Structure

- `app.py`: The main Streamlit application.
- `pdf_reader.py`: Handles PDF file processing.
- `prompts.py`: Contains prompt templates for the AI model.
- `resume_analyzer.py`: Core logic for analyzing resumes.
- `requirements.txt`: Lists all Python dependencies.
- `README.md`: This file.
