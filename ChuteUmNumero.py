import random
import PySimpleGUI as sg

class WhatTheNumber:
    def __init__(self):
        self.r_n = 0
        self.n_min = 1
        self.n_max = 100
        self.try_again = True

    def iniciar(self):
        # Layout
        self.layout = [
            [sg.Text("What is the number", size=(20,0))],
            [sg.Input(size=(18,0),key=("ValueR"))],
            [sg.Button("Try!")],
            [sg.Output(size=(20,10))]
        ]
        # Criar a jenla
        self.window = sg.Window("WTN", layout=self.layout)
        # Criar o numero
        self.RN()
        try:
            while True:
                self.WindowRead()
                if self.eventos == "Try!":
                    self.trie = self.valores['ValueR']
                    while self.try_again == True:
                        if int(self.trie) > self.r_n:
                            print("Down")
                            break
                        elif int(self.trie) < self.r_n:
                            print('UP')
                            break
                        if int(self.trie) == self.r_n:
                            self.try_again = False
                            print("Alright")

        except:
            print("only numbers pls")
            self.iniciar()





    # Ler valores da janela
    def WindowRead(self):
        self.eventos,self.valores = self.window.Read()
    # Gerar numero aleatorio
    def RN(self):
        self.r_n = random.randint(self.n_min, self.n_max)

what = WhatTheNumber()
what.iniciar()