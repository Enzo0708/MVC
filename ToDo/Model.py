class ToDo():  # Define a classe ToDo
    def __init__(self):  # Método construtor sem parâmetros
        self.lista = []  # Inicializa uma lista vazia para armazenar as tarefas

    def AdicionarTarefa(self, tarefa):  # Define o método AdicionarTarefa que recebe a tarefa como parâmetro
        self.lista.append(tarefa)  # Adiciona a tarefa à lista de tarefas
        return True  # Retorna True indicando que a tarefa foi adicionada com sucesso

    def ExcluirTarefa(self, excluir):  # Define o método ExcluirTarefa que recebe o índice da tarefa a ser excluída como parâmetro
        self.lista.pop(excluir)  # Remove a tarefa correspondente ao índice da lista de tarefas
        return True  # Retorna True indicando que a tarefa foi excluída com sucesso

    def ListarTarefas(self):  # Define o método ListarTarefas que não recebe nenhum parâmetro
        return self.lista  # Retorna a lista de tarefas
    
    def AlterarTarefa(self, alterar):
        self.lista.pop(alterar)
        return True
    

    def ConcluirTarefa(self, concluir):
        self.lista.pop(concluir)
        return True

    def ListarTarefasConcluidas(self,concluidas):
        #Somente as tarefas concluidas
        return self.lista
        


TODO = ToDo()  # Cria uma instância da classe ToDo e atribui à variável TODO