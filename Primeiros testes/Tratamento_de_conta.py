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
                x = linha.replace(' ','_').strip()

                # Fatiamento das colunas em indices
                divido = x[:6],x[8:19],x[25:57],x[77:84],x[84:116],x[117:122],x[132:141],x[142:152],x[181:]
                
                # Cabeçalho: Unidade, Irreg, Convênio, Razao, Código, Nome, Erro, BA, AT
                fim = divido[8],divido[0],divido[1],divido[2],divido[3],divido[4],divido[5],divido[6],divido[7]
                irreg = '|'.join(fim).replace('_',' ')
                if '||' not in irreg:
                    if '|Psp191|P' not in irreg:
                        if 'Adm|' not in irreg:
                            if '---|' not in irreg:
                                if '|K    |' in irreg:
                                    print(str(irreg.title()))

tela = TelaPython()
tela.Iniciar()