import re

def get_cnpj(lines):
    for line in lines:
        find_cnpj = re.search("\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}", line)
        if find_cnpj:
            cnpj = find_cnpj.group()
            break
    cnpj_to_find = cnpj
    return cnpj_to_find