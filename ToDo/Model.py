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
        tarefas = [tarefa for tarefa in tarefas if tarefa.status == "A fazer"]
        return tarefas
    
    def AlterarTarefa(self, alterar):       # Define o método AlterarTarefa que recebe o índice da tarefa a ser alterada e a nova descrição como parâmetros    
        self.lista.pop(alterar) # Remove a tarefa correspondente ao índice da lista de tarefas
        return True     # Retorna True indicando que a tarefa foi alterada com sucesso

    def ConcluirTarefa(self, concluir):    # Define o método ConcluirTarefa que recebe o índice da tarefa a ser concluída e o novo status como parâmetros
        self.lista_concluidos.pop(concluir) # Remove a tarefa correspondente ao índice da lista de tarefas
        return True    # Retorna True indicando que a tarefa foi concluída com sucesso
    
    def listar_tarefas_concluidas(tarefas): # Define o método listar_tarefas_concluidas que recebe a lista de tarefas como parâmetro
        tarefas_concluidas = [tarefa for tarefa in tarefas if tarefa.status == "Concluída"] # Cria uma lista com as tarefas concluídas
        return tarefas_concluidas   # Retorna a lista de tarefas concluídas
        


TODO = ToDo()  # Cria uma instância da classe ToDo e atribui à variável TODO