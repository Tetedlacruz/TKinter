from tkinter import *
import random

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")

        self.container1 = Frame(master, pady = 10)
        self.container1.pack()

        self.container2 = Frame(master, padx = 10)
        self.container2.pack()

        self.container3 = Frame(master, padx = 10)
        self.container3.pack()

        self.container4 = Frame(master, pady = 10)
        self.container4.pack()

        self.container5 = Frame(master, pady = 10)
        self.container5.pack()

        self.titulo = Label(self.container1, text='''      Sorteio Festa Das Cores 
        V1.1 
        GUI Version''', font = ("Arial", "10", "bold"))
        self.titulo.pack()

        self.nomeLabel = Label(self.container2,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.container2, width = 30, font = self.fontePadrao)
        self.nome.pack(side=LEFT)

        self.corLabel = Label(self.container3, text="Cor   ", font=self.fontePadrao)
        self.corLabel.pack(side=LEFT)

        self.cor2 = Entry(self.container3, width = 30, font = self.fontePadrao)
        self.cor2.pack(side=LEFT)

        self.enviar = Button(self.container4, text = "Enviar", 
    font = ("Calibri", "8"), width = 12, command = self.receber)
        self.enviar.pack(side=LEFT)

        self.sortear = Button(self.container4, text = "Sortear", 
    font = ("Calibri", "8"), width = 12, command = self.sorteio)
        self.sortear.pack(side=RIGHT)

        self.regras = Button(self.container5, text = "Regras", font = ("Calibri", "8"), 
    fg = "red", width = 12, command = self.regra)
        self.regras.pack()

        self.mensagem = Label(self.container4, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.nomes = []
        self.cores = []

    def regra(self):
        self.label = Label(self.container5, text='''
1. Só será sorteado a quantidade de      
cores digitadas.
2. Se houver mais nomes do que cores  
será sorteado aleatóriamente dois nomes 
para uma cor.
3. Se tiver mais cores do que nomes só 
será exibido a quantidade de nomes.''', font=self.fontePadrao, fg="red")
        self.label.pack()

    def receber(self):
        nome = self.nome.get()
        self.nomes.append(nome)
        self.nome.delete(0)
        cor = self.cor2.get()
        self.cores.append(cor)
        self.cor2.delete(0)
        print("Enviado")
        print(self.cores, self.nomes)

    def sorteio(self):
        while '' in self.nomes:
            self.nomes.remove('')
        while '' in self.cores:
            self.cores.remove('')
        while len(self.nomes) > len(self.cores):
            random.shuffle(self.nomes)
            random.shuffle(self.cores)
            self.titulo = Label(self.container1, text=f'''{self.nomes.pop(0)} e {self.nomes.pop(1)}
Cor = {self.cores.pop(0)}
--------------------''', font = ("Arial", "10", "bold"))
            self.titulo.pack(side=TOP)

        for i in range (len(self.cores)):
            if self.nomes == []:
                break
            random.shuffle(self.nomes)
            random.shuffle(self.cores)
            self.titulo = Label(self.container1, text=f'''{self.nomes.pop(0)}
Cor = {self.cores.pop(0)}
--------------------''', font = ("Arial", "10", "bold"))
            self.titulo.pack(side=BOTTOM)

root = Tk()
Application(root)
root.title("Festa das Cores")
root.mainloop()
