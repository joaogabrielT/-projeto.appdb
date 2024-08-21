import tkinter
from tkinter import *
class Principal:
        def __init__(self ,master=None):
            self.janela = Frame(master)
            self.janela["padx"] = 20
            self.janela.pack()

            self.usuarios = Button(self.janela)
            self.usuarios["text"] = "Usuários"
            self.usuarios["font"] = ("Calibri", "12")
            self.usuarios["width"] = 14
            self.usuarios.pack(side=LEFT)

            self.cidades = Button(self.janela)
            self.cidades["text"] = "Cidades"
            self.cidades["font"] = ("Calibri", "12")
            self.cidades["width"] = 14
            self.cidades.pack(side=LEFT)

            self.clientes = Button(self.janela)
            self.clientes["text"] = "Clientes"
            self.clientes["font"] = ("Calibri", "12")
            self.clientes["width"] = 14
            self.clientes.pack(side=LEFT)

            self.fechar = Button(self.janela)
            self.fechar["text"] = "Fechar"
            self.fechar["font"] = ("Calibri", "12")
            self.fechar["width"] = 14
            self.fechar.pack(side=LEFT)


root = Tk()
Principal(root)
root.state("zoomed")
root.mainloop()
