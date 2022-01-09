from docxtpl import DocxTemplate
import pandas as pd
from time import sleep
from datetime import datetime, date

#? Importação do Template e da Planilha.
doc = DocxTemplate('CFA-Carta_Fatura_Automática\Entrada\Template.docx')
base = pd.read_excel('CFA-Carta_Fatura_Automática\Entrada\Recibo_fatura-backoffice.xls')


#? Inicia o Laço que irá percorrer cada linha do Data Frame.
print('Iniciando Função')
sleep(1)
def Carta_Automatica():
    index = 0
    for i in range(len(base)):
        primeira_linha = base.iloc[index]
        index = index + 1
        context = dict(primeira_linha)

        #? Extrai o dado de cada linha para ser usado no nome do novo arquivo.
        numero_SOE = primeira_linha['ID']
        cnpj = primeira_linha['CNPJ']
        n_carta = primeira_linha['Carta_fatura']

        nome_do_arquivo = f'Carta_Fatura ID {int(numero_SOE)} N°{int(n_carta)} CNPJ {int(cnpj)}.docx'

        #? Renderiza e salva o Doc.
        doc.render(context)
        doc.save(f'CFA-Carta_Fatura_Automática\Saida_Carta\ {nome_do_arquivo}')
        print(f'Carta {int(n_carta)} criada com sucesso!')
        sleep(0.5)


def Recibo_Automatico():
    pass

Carta_Automatica()