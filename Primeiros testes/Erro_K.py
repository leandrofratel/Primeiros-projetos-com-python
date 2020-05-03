import PySimpleGUI as sg

class TelaPython:#Parte grafica
    def __init__(self):
        # Definição de cor
        sg.change_look_and_feel('DarkBlue')
        # Layout
        layout = [
            [sg.Text('Endereço do Arquivo',size=(15,0)),sg.Input(size=(52,0),key='txt')],
            [sg.Button('Confirmar')],
            [sg.Output(size=(120,20))]
        ]
        # Janela
        self.janela = sg.Window("Tratamento de Contas").layout(layout)

    def Iniciar(self):
        while True:
            # Extração de dados para tratamento
            self.button, self.values = self.janela.Read()
            texto = self.values['txt']
            with open(texto, encoding='ANSI') as arquivo:
                linhas = arquivo.readlines()

            irreg = []
            # Cabeçalho
            print('Unidade|Irreg|Convênio|Razao|Código|Nome|Erro|BA|AT')

            for linha in linhas:
                if ' K    ' in linha:
                    relatorio = linha[173:178], linha[:6], linha[8:18], 
                    linha[25:57], linha[76:83], linha[84:111], linha[116:122], 
                    linha[129:140], linha[141:151]
                    
                    novo_relatorio = '|'.join(relatorio)
                    print(str(novo_relatorio.title()))

tela = TelaPython()
tela.Iniciar()