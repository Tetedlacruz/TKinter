from CRUD_GUI import Usuarios
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master, pady = 10)
        self.container1.pack()

        self.container2 = Frame(master, padx = 20, pady = 5)
        self.container2.pack()

        self.container3 = Frame(master, padx = 20, pady = 5)
        self.container3.pack()

        self.container4 = Frame(master, padx = 20, pady = 5)
        self.container4.pack()

        self.container5 = Frame(master, padx = 20, pady = 5)
        self.container5.pack()

        self.container6 = Frame(master, padx = 20, pady = 5)
        self.container6.pack()

        self.titulo = Label(self.container1, text="Informe os dados :", 
        font = ("Calibri", "9", "bold"))
        self.titulo.pack()

        self.lblid = Label(self.container2,
        text="ID:", font=self.fonte, width=10)
        self.lblid.pack(side=LEFT)

        self.txtid = Entry(self.container2, width = 10, 
        font = self.fonte)
        self.txtid.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",
        font=self.fonte, width=10, command = self.buscarUsuario, fg = "blue")
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:",
        font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3, width = 25,
        font = self.fonte)
        self.txtnome.pack(side=LEFT)

        self.lbltelefone = Label(self.container4, text="CPF:",
        font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)

        self.txtcpf = Entry(self.container4, width = 25, 
        font = self.fonte)
        self.txtcpf.pack(side=LEFT)

        self.bntInsert = Button(self.container5, text="Inserir",
        font=self.fonte, width=12, command = self.inserirUsuario, fg= "green")
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container5, text="Alterar",
        font=self.fonte, width=12, command = self.alterarUsuario, fg= "gray")
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container5, text="Excluir",
        font=self.fonte, width=12, command = self.excluirUsuario, fg= "red")
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container6, text="", 
        font = ("Verdana", "9", "italic"))
        self.lblmsg.pack()

    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.txtnome.get()
        user.cpf = self.txtcpf.get()

        self.lblmsg["text"] = user.insertUser()
        self.txtid.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)

    def alterarUsuario(self):
        user = Usuarios()
        user.id = self.txtid.get()
        user.nome = self.txtnome.get()
        user.cpf = self.txtcpf.get()

        self.lblmsg["text"] = user.updateUser()
        self.txtid.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)

    def excluirUsuario(self):
        user = Usuarios()
        user.id = self.txtid.get()

        self.lblmsg["text"] = user.deleteUser()
        self.txtid.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.txtid.get()
    
        self.lblmsg["text"] = user.selectUser(idusuario)
        self.txtid.delete(0, END)
        self.txtid.insert(INSERT, user.id)
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)
        self.txtcpf.delete(0, END)
        self.txtcpf.insert(INSERT,user.cpf)

root = Tk()
Application(root)
root.title("Banco de Dados")
root.mainloop()