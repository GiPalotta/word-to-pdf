import os
from docx2pdf import convert

def conversor(dir_entrada, dir_saida):
    if not os.path.exists(dir_saida):
        os.mkdir(dir_saida)

    for nome_arquivo in os.listdir(dir_entrada):
        if nome_arquivo.endswith('.docx'):
            dir_entrada = os.path.join(dir_entrada, nome_arquivo)
            dir_saida = os.path.join(dir_saida, nome_arquivo.replace('.docx', '.pdf'))

            convert(dir_entrada, dir_saida)

dir_entrada = 'Projetos/Arquivos'
dir_saida = 'Projetos/Arquivos'

conversor(dir_entrada, dir_saida)