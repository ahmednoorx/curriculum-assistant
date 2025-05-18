# Curriculum Assistant

This project is a Curriculum Assistant built with Streamlit that leverages open-source models for text generation and supports PDF/DOCX parsing. It provides functionalities to generate text based on user prompts, parse documents, and export content in various formats.

## Features

- **Text Generation**: Utilizes open-source models (e.g., Falcon via Groq or Hugging Face) to generate text based on user input.
- **PDF Parsing**: Extracts text from PDF files for easy manipulation and analysis.
- **DOCX Parsing**: Extracts text from DOCX files, allowing users to work with Microsoft Word documents.
- **Export Options**: Users can export generated content as PDF or DOCX files.

## Project Structure

```
curriculum-assistant
├── src
│   ├── app.py               # Main entry point for the Streamlit application
│   ├── models
│   │   └── text_generation.py # Text generation model integration
│   ├── parsers
│   │   ├── pdf_parser.py     # PDF file parsing functionality
│   │   └── docx_parser.py    # DOCX file parsing functionality
│   ├── exporters
│   │   ├── export_pdf.py     # PDF export functionality
│   │   └── export_docx.py    # DOCX export functionality
│   └── utils
│       └── helpers.py        # Utility functions
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
└── .gitignore                # Git ignore file
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/curriculum-assistant.git
   cd curriculum-assistant
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```
   streamlit run src/app.py
   ```

2. Follow the on-screen instructions to use the text generation, parsing, and exporting features.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.