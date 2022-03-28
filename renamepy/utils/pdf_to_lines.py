import pdfplumber
import identify_file_department
from utils.process_files import process_notidentified_pdf_files

def lines_from_pdf(file):
    pdf = file
    with pdfplumber.open(pdf) as pdf:
        page = pdf.pages[0]
        text = page.extract_text(x_tolerance=1)
        try:
            lines = text.split('\n')
            pdf.close()
            identify_file_department.identify_department(lines, file)
        except AttributeError:
            print('Erro de atributo')
            print("Não identificado\n")
            pdf.close()
            process_notidentified_pdf_files(file)