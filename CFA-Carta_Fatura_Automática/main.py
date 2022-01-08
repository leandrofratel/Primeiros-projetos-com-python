from docxtpl import DocxTemplate
import pandas as pd

#! Importação do Template e da Planilha.
doc = DocxTemplate('CFA-Carta_Fatura_Automática\Entrada\Template.docx')
base = pd.read_excel('CFA-Carta_Fatura_Automática\Entrada\Base.xlsx')

data = base.to_dict(orient='list')
for linha in data:
    context = data

#! Renderiza e salva o Doc.
doc.render(context)
doc.save('CFA-Carta_Fatura_Automática\Saida\Carta_Fatura_Pronta.docx')
print('Arquivo criado com sucesso!')