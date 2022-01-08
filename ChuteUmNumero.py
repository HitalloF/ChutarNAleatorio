import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.numero_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def iniciar(self):

        # layout
        self.layout = [
            [sg.Text('Insira um numero',size=(20,0))],
            [sg.Input(size=(18,0),key="ValorChute")],
            [sg.Button('Chutar!')],
            [sg.Output(size=(20,10))]
        ]
        # Criar uma janela
        self.janela = sg.Window('Chute o Numero', layout=self.layout)

        self.GerarNumeroAleatroio()

        try:
            while True:

                self.LerValoresDaTela()
                 # Fazer alguma coisa com esse valores
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.numero_aleatorio:
                            print("Chute numero mais baixo")

                            break
                        elif int(self.valor_do_chute) < self.numero_aleatorio:
                            print("Chute um numero mais alto")

                            break
                        if int(self.valor_do_chute) == self.numero_aleatorio:
                            self.tentar_novamente = False
                            print('Acertou :3')
                            break
        except :
            print('Favor Digitar apenas numeros')
            self.iniciar()


    def LerValoresDaTela(self):
        # Receber VAlores
        self.evento, self.valores = self.janela.Read()
    def GerarNumeroAleatroio(self):
        self.numero_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)


chute = ChuteONumero()
chute.iniciar()