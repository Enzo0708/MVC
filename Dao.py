class Dao:
    def __init__ (self):
        self.arquivo  = "tarefas.txt"

    def AdicionarTarefa(self, tarefa):
        try:
            with open(self.arquivo, "a") as arquivo:
                arquivo.write(tarefa + "\n")
                return True

        except Exception as error:
            print(error.__class__.__name__)
            return False
        
    def listarTarefas(self):
        try:
            with open(self.arquivo, "r") as arquivo:
                return arquivo.readlines()

        except Exception as error:
            print(error.__class__.__name__)
            return False

DAO = Dao()