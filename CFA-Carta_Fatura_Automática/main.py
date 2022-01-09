from docxtpl import DocxTemplate
import pandas as pd
from time import sleep

#? Importação do Template e da Planilha.
doc = DocxTemplate('CFA-Carta_Fatura_Automática\Entrada\Template.docx')
base = pd.read_excel('CFA-Carta_Fatura_Automática\Entrada\Recibo_fatura-backoffice.xls')

#? Inicia o Laço que irá percorrer cada linha do Data Frame.
def Carta_Automatica():
    index = 0
    for i in range(len(base)):
        primeira_linha = base.iloc[index]
        index = index + 1
        context = dict(primeira_linha)

        #? Extrai o dado de cada linha para ser usado no nome do novo arquivo.
        numero_SOE = primeira_linha['ID']

        nome_do_arquivo = f'Carta_Fatura ID {numero_SOE}.docx'

        #? Renderiza e salva o Doc.
        doc.render(context)
        doc.save(f'CFA-Carta_Fatura_Automática\Saida\ {nome_do_arquivo}')
        print(f'Arquivo {numero_SOE} criado com sucesso!')
        sleep(1)

def Recibo_Automatico():
    pass

Carta_Automatica()