from datetime import datetime
from utils.get_cnpj import get_cnpj
from utils.process_files import process_file

def set_das_properties(lines, file):
    kind = 'GUI'
    dept = 'FSC'
    desc = 'DAS'
    doc_infos = lines[5].split(' ')
    competencia = doc_infos[0].upper().replace('/', '-')
    year = datetime.today().strftime('%Y%m%d')
    name_without_code = '_'+kind+'_'+dept+'_'+desc+'-'+competencia+'_'+year+'.pdf'
    process_file(name_without_code, get_cnpj(lines), file)