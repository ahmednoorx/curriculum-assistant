class PDFParser:
    def extract_text(self, pdf_file):
        import PyPDF2
        
        text = ""
        with open(pdf_file, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text.strip()