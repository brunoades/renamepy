import set_fsc_files
from utils.process_files import process_notidentified_pdf_files

def indetify_fsc_kind(lines, line, file):
    if line == 1:
        print("Este é um documento de DAS: " + file.name)
        set_fsc_files.set_das_properties(lines, file)