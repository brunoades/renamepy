import re

def get_caixakey(lines):
    for line in lines:
        find_key = re.search("\w{2}\-\d{11}\-\d{8}\-\d{2}", line)
        if find_key:
            key = find_key.group()
            break
        else:
            key = ''
    return key