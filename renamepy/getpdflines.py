import pdfplumber
import re
file = f'.\\renamepy\\source\\ExampleFile.pdf'

def get_pdf_structure():
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[0]
        text = page.extract_text(x_tolerance=2)
        lines = text.split('\n')
        for line in lines:
            find_cnpj = re.search("\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}", line)
            if find_cnpj:
                cnpj = find_cnpj.group()
                break
        print(cnpj)
get_pdf_structure()

def get_pdf_lines():
    with pdfplumber.open(file) as pdf:
        page = pdf.pages[0]
        text = page.extract_text(x_tolerance=2)
        lines = text.split('\n')
        for line in lines:
            print(line)
get_pdf_lines()

