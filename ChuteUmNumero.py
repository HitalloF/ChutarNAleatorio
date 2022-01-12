import random
import PySimpleGUI as sg
class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def iniciar(self):
        # layout
        self.layout = [
            [sg.Text("Chute o Numero", size=(25,0))],
            [sg.Input(size=(22,0), key="ValorChute")],
            [sg.Button("Chutar!")],
            [sg.Output(size=(20,20))]
        ]
        self.janela = sg.Window("Chute!", layout=self.layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                self.LerValoresNaJanela()
                if self.eventos == "Chutar!":
                    self.valor_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_chute) > self.valor_aleatorio:
                            print("Digite um numero menor")
                            break
                        elif int(self.valor_chute) < self.valor_aleatorio:
                            print("Digite um numero maior")
                            break
                        if int(self.valor_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print("Acertou!")
                            break
        except:
            print("Digite Apenas numeros")
            self.iniciar()

    def LerValoresNaJanela(self):
        self.eventos,self.valores = self.janela.Read()
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.iniciar()