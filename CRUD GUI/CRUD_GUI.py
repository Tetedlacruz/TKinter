class Banco():

    def __init__(self):
        import sqlite3
        self.conexao = sqlite3.connect('moleza.sqlite')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS pessoas (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT ,
                    nome TEXT,
                    cpf TEXT)""")
        self.conexao.commit()
        c.close()

class Usuarios(object):

    def __init__(self, id = 0, nome = "", cpf = ""):
        self.info = {}
        self.id = id
        self.nome = nome
        self.cpf = cpf

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO pessoas (nome, cpf) VALUES ('" + self.nome + "', '" +
            self.cpf + "' )")
            banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"

        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("UPDATE pessoas SET nome = '" + self.nome + "', cpf = '" + 
            self.cpf + "' WHERE id = " + self.id + " ")
            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"

        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM pessoas WHERE id = " + self.id + " ")
            banco.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"

        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, id):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM pessoas where id = " + id + "  ")
            for linha in c:
                self.id = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
            c.close()
            return "Busca feita com sucesso!"

        except:
            return "Ocorreu um erro na busca do usuário"