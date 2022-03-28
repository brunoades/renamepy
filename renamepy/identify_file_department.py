import os
from identify_cnd_kinds import indentify_cnd_kind
from identify_dpp_kinds import identify_ddp_kind
from identify_fsc_kinds import indetify_fsc_kind
import identify_leg_kinds
import identify_ots_kinds
from utils.get_departments import *
from utils.process_files import process_notidentified_pdf_files

# cnd_comparators = {'Documento de CND' : 1}
cnd_comparators = get_cnd_comparators()

ctb_comparators = {'Documento do Contábil' : 1}

dpp_comparators = get_dpp_comparators()

fsc_comparators = {'do Simples Nacional' : 1}
leg_comparators = {'Documento da Legalização' : 1}
ots_comparators = {'Documento de Outros' : 1}

def identify_department(lines, file):
    department = ''
    for line in lines:
        if line in cnd_comparators.keys():
            department = 'CND'
            break
        if line in ctb_comparators.keys():
            department = 'CTB'
            break
        if line in dpp_comparators.keys():
            department = 'DPP'
            break
        if line in fsc_comparators.keys():
            department = 'FSC'
            break
        if line in leg_comparators.keys():
            department = 'LEG'
            break
        if line in ots_comparators.keys():
            department = 'OTS'
            break

    if department == 'CND':
        print('CND')
        indentify_cnd_kind(lines, cnd_comparators[line], file)
    elif department == 'CTB':
        print('CTB')
    elif department == 'DPP':
        identify_ddp_kind(lines, dpp_comparators[line], file)
    elif department == 'FSC':
        print('FSC')
        indetify_fsc_kind(lines, fsc_comparators[line], file)
    elif department == 'LEG':
        print('LEG')
    else:
        print('Não identificado!')
        process_notidentified_pdf_files(file)