from datetime import datetime
from utils.dpp_utils import *
from utils.get_cnpj import get_cnpj
from utils.process_files import process_file

year = datetime.today().strftime('%Y%m%d')

def set_fgts_properties(lines, file):
    kind = 'DEM'
    dept = 'DPP'
    desc = 'FGTS'
    name_on_line = lines[11]
    name = name_on_line[6:].replace(" ", "")
    name_without_code = '_'+kind+'_'+dept+'_'+desc+'-'+name+'_'+year+'.pdf'
    process_file(name_without_code, get_cnpj(lines), file)

def set_grrf_properties(lines, file):
    kind = 'GUI'
    dept = 'DPP'
    desc = 'GRRF'
    name_without_code = '_'+kind+'_'+dept+'_'+desc+'_'+year+'.pdf'
    process_file(name_without_code, get_cnpj(lines), file)

def set_grf_properties(lines, file):
    kind = 'GUI'
    dept = 'DPP'
    desc = 'GRF'
    name_without_code = '_'+kind+'_'+dept+'_'+desc+'_'+year+'.pdf'
    process_file(name_without_code, get_cnpj(lines), file)

def set_aviso_previo_indenizado_properties(lines, file):
    kind = 'AVS'
    dept = 'DPP'
    desc = 'RCT'
    name_on_line = lines[3]
    name = name_on_line[7:].replace(" ", "")
    name_without_code = '_'+kind+'_'+dept+'_'+desc+'-'+ name + '_'+year+'.pdf'
    process_file(name_without_code, get_cnpj(lines), file)

def set_movimentacao_trabalhador(lines, file):
    kind = 'CHV'
    dept = 'DPP'
    desc = 'MOVIMENTACAO'
    name_on_line = lines[10]
    name = name_on_line[13:].replace(" ", "")
    id_key_full = get_caixakey(lines).split('-')
    id_key = id_key_full[2]
    name_without_code = '_'+kind+'_'+dept+'_'+desc+'-'+ name + '-' + id_key + '_'+year+'.pdf'
    process_file(name_without_code, get_cnpj(lines), file)
    # print(name_without_code)
    # print(id_key_full)

def set_verbas_rescisorias(lines, file):
    kind = 'CPV'
    dept = 'DPP'
    desc = 'RESCISAO'
    name_on_line = lines[1].split(',')
    name = name_on_line[1].replace(' ', '')
    name_without_code = '_'+kind+'_'+dept+'_'+desc+'-'+ name + '_'+year+'.pdf'
    process_file(name_without_code, get_cnpj(lines), file)

def set_requeriemnto_sd(lines, file):
    kind = 'REQ'
    dept = 'DPP'
    desc = 'SD'
    name_on_line = lines[5]
    name = name_on_line.replace(" ", "")
    name_without_code = '_'+kind+'_'+dept+'_'+desc+'-'+ name + '_'+year+'.pdf'
    process_file(name_without_code, get_cnpj(lines), file)

def set_extrato_fgts(lines, file):
    kind = 'EXT'
    dept = 'DPP'
    desc = ''
    name_on_line = lines[3]
    name = name_on_line[6:].replace(' ', '')
    name_without_code = '_'+kind+'_'+dept+'_'+ name + '_'+year+'.pdf'
    process_file(name_without_code, get_cnpj(lines), file)

def set_extrato_fgts_trabalhador(lines, file):
    kind = 'EXT'
    dept = 'DPP'
    desc = ''
    name_on_line = lines[1]
    name = name_on_line[5:].replace(' ', '')
    name_without_code = '_'+kind+'_'+dept+'_'+ name + '_'+year+'.pdf'
    process_file(name_without_code, get_cnpj(lines), file)

def set_atualizacao_ctps(lines, file):
    kind = 'FCH'
    dept = 'DPP'
    desc = 'CTPS'
    name_on_line = lines[10].split('-')
    name = name_on_line[1].replace(' ', '')
    name_without_code = '_'+kind+'_'+dept+'_'+desc+'-'+ name[:-19] + '_'+year+'.pdf'
    process_file(name_without_code, get_cnpj(lines), file)

def set_calculo_rescisao(lines, file):
    kind = 'RLT'
    dept = 'DPP'
    desc = 'ANALITICO'
    name_on_line = lines[5].split('-')
    name = name_on_line[1].replace(' ', '')
    name_without_code = '_'+kind+'_'+dept+'_'+desc+'-'+ name[:-17] + '_'+year+'.pdf'
    process_file(name_without_code, get_cnpj(lines), file)

def set_homologacao_rescisao(lines, file):
    kind = 'TRM'
    dept = 'DPP'
    desc = 'HOMOLOGACAO'
    name_on_line = lines[6]
    name = name_on_line.replace(' ', '')
    name_without_code = '_'+kind+'_'+dept+'_'+desc+'-'+ name[14:] + '_'+year+'.pdf'
    process_file(name_without_code, get_cnpj(lines), file)

def set_quitacao_rescisao(lines, file):
    kind = 'TRM'
    dept = 'DPP'
    desc = 'QUITACAO'
    name_on_line = lines[6]
    name = name_on_line.replace(' ', '')
    name_without_code = '_'+kind+'_'+dept+'_'+desc+'-'+ name[14:] + '_'+year+'.pdf'
    process_file(name_without_code, get_cnpj(lines), file)

def set_termo_rescisao(lines, file):
    kind = 'TRM'
    dept = 'DPP'
    desc = 'RESCISAO'
    name_on_line = lines[10]
    name = name_on_line.replace(' ', '')
    name_without_code = '_'+kind+'_'+dept+'_'+desc+'-'+ name[14:] + '_'+year+'.pdf'
    process_file(name_without_code, get_cnpj(lines), file)

def set_protocolo_conectividade(lines, file):
    kind = 'PRT'
    dept = 'DPP'
    desc = 'GRRF'
    name_on_line = lines[10]
    name = name_on_line.replace(' ', '')
    name_without_code = '_'+kind+'_'+dept+'_'+desc+'-' + '_'+year+'.pdf'
    process_file(name_without_code, get_cnpj(lines), file)