import set_dpp_files
from utils.process_files import process_notidentified_pdf_files

def identify_ddp_kind(lines, line, file):
    linha_recibo = lines[0]
    recibo = linha_recibo[:6]
    # 1
    if line == 1:
        print("Este é um documento de FGTS: " + file.name)
        set_dpp_files.set_fgts_properties(lines, file)
    # 2
    elif line == 2:
        print("Este é um documento GRRF - Guia de Recolhimento Rescisório do FGTS: " + file.name)
        set_dpp_files.set_grrf_properties(lines, file)
    # 3
    elif line == 3:
        print("Este é um documento de GRF: " + file.name)
        set_dpp_files.set_grf_properties(lines, file)
    # 4 TO-DO
    # 5 AVISO PRÉVIO DO EMPREGADOR PARA DISPENSA DO EMPREGADO
    elif line == 5:
        print("Este é um documento de Aviso prévio indenizado: " + file.name)
        set_dpp_files.set_aviso_previo_indenizado_properties(lines, file)
    # 6 TO-DO
    # 7
    elif line == 7:
        print("Este é um documento de Movimentação do trabalhador: " + file.name)
        set_dpp_files.set_movimentacao_trabalhador(lines, file)
    # 8 Comprovante de devolução da Carteira de Trabalho e Previdência Social
    #9
    elif line == 9:
        print("Este é um extrato do fundo de garantia: " +file.name)
        set_dpp_files.set_extrato_fgts_trabalhador(lines, file)
    # 10
    elif line == 10:
        print("Este é um de atualização da CTPS: " + file.name)
        set_dpp_files.set_atualizacao_ctps(lines, file)
    # 11
    # elif recibo == line:
    #     print("Este é um recibo de pagamento de verbas rescisorias: " + file)
    #     set_dpp_files.set_verbas_rescisorias(lines, file)
    # 12
    elif line == 12:
        print("Este é um documento de Requerimento de Seguro-Desemprego - SD: " +file.name)
        set_dpp_files.set_requeriemnto_sd(lines, file)
    # 13
    # elif lines[1] == line:
    #     print("Este é um extrato do fundo de garantia: " +file)
    #     set_dpp_files.set_extrato_fgts(lines, file)
    
    
    # elif lines[4] == line:
    #     print("Este é Relatório Analítico do Cálculo de Rescisão: " +file)
    #     set_dpp_files.set_calculo_rescisao(lines, file)
    # elif lines[0] == line:
    #     print("Este é TERMO DE HOMOLOGAÇÃO DE RESCISÃO DO CONTRATO DE TRABALHO: " +file)
    #     set_dpp_files.set_homologacao_rescisao(lines, file)
    # elif lines[0] == line:
    #     print("Este é TERMO DE QUITAÇÃO DE RESCISÃO DO CONTRATO DE TRABALHO: " +file)
    #     set_dpp_files.set_quitacao_rescisao(lines, file)
    # 18
    elif line == 18:
        print("Este é TERMO DE RESCISÃO DO CONTRATO DE TRABALHO: " +file.name)
        set_dpp_files.set_termo_rescisao(lines, file)
    # 19
    # elif lines[1] == line:
    #     print("Este é um Protocolo de Envio de Arquivos do CONECTIVIDADE SOCIAL: " +file)
    #     set_dpp_files.set_protocolo_conectividade(lines, file)
    
    else:
        process_notidentified_pdf_files(file)