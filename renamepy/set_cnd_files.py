from datetime import datetime
import re
from utils.get_cnpj import get_cnpj
from utils.process_files import process_file

year = datetime.today().strftime('%Y%m%d')

def get_rfbcode(line):
    # for line in lines:
    find_code = re.search("\w{4}\.\w{4}\.\w{4}\.\w{4}", line)
    if find_code:
        code = find_code.group().replace('.', '')
        # break
    else:
        code = ''
    return code

def get_rfbexpiration(line):
    find_expiration = re.search("\d{2}\/\d{2}\/\d{4}", line)
    if find_expiration:
        expiration = find_expiration.group().replace('/', '')
    else:
        expiration = ''
    return expiration


def set_cndrfd_properties(lines, file):
    kind = 'CND'
    dept = 'RFB'
    desc = 'NEGATIVA'
    control_code_line = len(lines) -2
    control_code = get_rfbcode(lines[control_code_line]) # line 24
    valid_until = get_rfbexpiration(lines[control_code_line -1]) # line 23
    name_without_code = '_'+kind+'_'+dept+'_'+desc+'-'+control_code+'-'+valid_until+'_'+year+'.pdf'
    process_file(name_without_code, get_cnpj(lines), file)