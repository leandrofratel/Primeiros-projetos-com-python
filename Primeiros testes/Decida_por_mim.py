# Projeto - Decida por mim
# Faça uma pergunta para o programa responder
import random

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
        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))

decida = DecidaPorMim()
decida.Iniciar()
