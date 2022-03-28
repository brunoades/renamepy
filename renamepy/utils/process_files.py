import os
from pathlib import Path
from datetime import datetime
from db.db_config import find_client

watch_folder = Path("renamepy/files/")
dest_folder = Path("renamepy/dest/")
ignore_dir = Path("renamepy/not_identified/")
extension  = '.pdf'

def process_file(name_without_code, cnpj_to_find, file):
    code = find_client(cnpj_to_find)
    name = code + name_without_code
    try:
        os.rename(file, dest_folder / name)
    except Exception as err:
        if err == 'WinError 183':
            hour = datetime.today().strftime('%H%M%S')
            name = code + name_without_code.replace('.pdf', '')
            fullName = name + hour + extension
            os.rename(file, dest_folder / fullName)
        pass

def process_notpdf_files(file):
    try:
        print("Process not pdf files")
        print(file)
        os.rename(file, ignore_dir / file.name)
    except Exception as err:
        name_sulfix = datetime.today().strftime('%Y%m%d%H%M%S' + file.suffix)
        name = file.stem + '_' + name_sulfix
        os.rename(file, ignore_dir / name)

def process_notidentified_pdf_files(file):
    try:
        os.rename(file, ignore_dir / file.name)
    except Exception as err:
        name_sulfix = datetime.today().strftime('%Y%m%d%H%M%S' + file.suffix)
        name = file.stem + '_' + name_sulfix
        os.rename(file, ignore_dir / name)
        print(err)
        pass

def process_duplicated_files(file):
    print(file)