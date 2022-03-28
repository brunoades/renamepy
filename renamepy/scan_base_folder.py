import os
from utils.pdf_to_lines import lines_from_pdf
from utils.process_files import process_notpdf_files

def scan_base_dir(dir):
    with os.scandir(dir) as files:
        for file in files:
            if file.name.endswith('.pdf') or file.name.endswith('.PDF') and file.is_file():
                lines_from_pdf(dir / file.name)
            else:
                print("Arquivo não PDF\n")
                print(dir / file.name)
                process_notpdf_files(dir / file.name)
                