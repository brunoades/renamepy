import set_cnd_files
from utils.process_files import process_notidentified_pdf_files

def indentify_cnd_kind(lines, line, file):
    if line == 1:
        print("Este é um documento de CND do Ministério da Fazenda " + file.name)
        set_cnd_files.set_cndrfd_properties(lines, file)
    else:
        print("CND de tipo não configurado!")