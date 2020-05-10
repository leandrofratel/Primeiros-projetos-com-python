# Projeto - Chute o número
# Algoritimo que cria um numero aletório de 1 a 100 e pede para você advinhar.
import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu chute',size=(20,0))],
            [sg.Input(size=(10,0),key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(30,10))]
        ]
        # Cria uma janela
        self.janela = sg.Window('Chute um número',layout=layout)
        self.GeradorNumeroAleatorio()
        try:
            while True:
                # Recebe Valores
                self.evento, self.valores = self.janela.Read()
                # Interação com os valores
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valo menor!')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto!')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('Parabens você acertou!')
                            break
        except:
            print('Favor digitar apenas números!')
            self.Iniciar()

    def GeradorNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()