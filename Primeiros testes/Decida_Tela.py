# Projeto - Decida por mim
# Faça uma pergunta para o programa responder
import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você que sabe.',
            'Não faz isso!',
            'Faz isso!',
            'Acho que ta na hora certa!'
        ]

    def Iniciar(self):
        # Tema
        sg.change_look_and_feel('DarkBlue')
        # Layout
        layout =[
            [sg.Text('Faça uma pergunta: ')],
            [sg.Input()],
            [sg.Output(size=(50,10))],
            [sg.Button('Decidir')]
        ] 
        # Janela
        self.janela = sg.Window('Decida Por Mim',layout=layout)
        while True:
            # Ler os valores
            self.evento, self.valores = self.janela.Read()
            # Fazer algo com os valores
            if self.evento == 'Decidir':
                print(random.choice(self.respostas))

decida = DecidaPorMim()
decida.Iniciar()