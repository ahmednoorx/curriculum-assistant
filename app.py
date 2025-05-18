from src.models.text_generation import TextGenerator
from src.parsers.pdf_parser import PDFParser
from src.parsers.docx_parser import DOCXParser
from src.exporters.export_pdf import PDFExporter
from src.exporters.export_docx import DOCXExporter
import streamlit as st

def main():
    st.title("Curriculum Assistant")
    
    st.sidebar.header("Options")
    option = st.sidebar.selectbox("Choose an action", ["Generate Text", "Parse File", "Export Content"])

    if option == "Generate Text":
        prompt = st.text_area("Enter your prompt:")
        if st.button("Generate"):
            text_generator = TextGenerator()
            generated_text = text_generator.generate_text(prompt)
            st.text_area("Generated Text", generated_text, height=300)

    elif option == "Parse File":
        uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])
        if uploaded_file is not None:
            if uploaded_file.type == "application/pdf":
                pdf_parser = PDFParser()
                extracted_text = pdf_parser.extract_text(uploaded_file)
                st.text_area("Extracted Text", extracted_text, height=300)
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                docx_parser = DOCXParser()
                extracted_text = docx_parser.extract_text(uploaded_file)
                st.text_area("Extracted Text", extracted_text, height=300)

    elif option == "Export Content":
        content = st.text_area("Enter content to export:")
        export_type = st.selectbox("Select export format", ["PDF", "DOCX"])
        if st.button("Export"):
            if export_type == "PDF":
                pdf_exporter = PDFExporter()
                pdf_exporter.export(content, "exported_content.pdf")
                st.success("Content exported as PDF.")
            elif export_type == "DOCX":
                docx_exporter = DOCXExporter()
                docx_exporter.export(content, "exported_content.docx")
                st.success("Content exported as DOCX.")

if __name__ == "__main__":
    main()