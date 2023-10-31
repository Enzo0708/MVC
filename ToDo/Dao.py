class Dao:  # Define a classe Dao
    def __init__ (self):  # Método construtor sem parâmetros
        self.arquivo  = "tarefas.txt"  # Define o nome do arquivo onde as tarefas serão armazenadas
        with open (self.arquivo, "a") as arquivo:
            arquivo.close()

    def AdicionarTarefa(self, tarefa):  # Define o método AdicionarTarefa que recebe a tarefa como parâmetro
        try:  # Tenta executar o bloco de código dentro do try

            with open(self.arquivo, "a") as arquivo:  # Abre o arquivo em modo de anexação ("a")
                arquivo.write(tarefa) # Escreve a tarefa no arquivo seguida de uma quebra de linha
                #O Arquivo ter como padrão ja escrito ID - Tarefa
                
                return True  # Retorna True indicando que a tarefa foi adicionada com sucesso

        except Exception as error:  # Se ocorrer um erro durante a execução do bloco de código dentro do try
            print(error.__class__.__name__)  # Imprime o nome da classe do erro
            return False  # Retorna False indicando que a tarefa não foi adicionada com sucesso
        
    # Define o método listar Tarefas que não recebe nenhum parâmetro
    def listarTarefas(self):
        try:  # Tenta executar o bloco de código dentro do try
            # Abre o arquivo em modo de leitura ("r")
            with open(self.arquivo, "r") as arquivo:
                # Retorna uma lista contendo todas as linhas do arquivo
                return arquivo.readlines()
        except Exception as error:  # Se ocorrer um erro durante a execução do bloco de código dentro do try
            # Imprime o nome da classe do erro
            print(error.__class__.__name__)
            # Retorna False indicando que as tarefas não foram listadas com sucesso
            return False

    # Define o método excluirTarefa que recebe o índice da tarefa a ser excluída como parâmetro
    def excluirTarefa(self, excluir):
        try:
            # Abre o arquivo em modo de leitura ("r")
            with open(self.arquivo, "r") as arquivo:
                # Lê todas as linhas do arquivo e armazena em uma lista
                tarefas = arquivo.readlines()
                # Remove a tarefa com o índice especificado da lista
                tarefas.pop(excluir)
            # Abre o arquivo em modo de escrita ("w")
            with open(self.arquivo, "w") as arquivo:
                # Escreve todas as tarefas da lista no arquivo
                for tarefa in tarefas:
                    arquivo.write(tarefa)
            return True
        except Exception as error:
            print(error.__class__.__name__)
            return False

    # Define o método alterarTarefa que recebe o índice da tarefa a ser alterada e a nova descrição como parâmetros
    def alterarTarefa(self, indice, nova_descricao):
        try:
            # Abre o arquivo em modo de leitura ("r")
            with open(self.arquivo, "r") as arquivo:
                # Lê todas as linhas do arquivo e armazena em uma lista
                tarefas = arquivo.readlines()
            # Verifica se o índice especificado é válido
            if indice >= 0 and indice < len(tarefas):
                # Extrai as partes da tarefa
                tarefa_parts = tarefas[indice].split(" - ", 2)
                if len(tarefa_parts) == 3:
                    id, status, descricao = tarefa_parts  # Extrai as partes da tarefa
                    # Atualiza somente a descrição mantendo id e status
                    tarefa_atualizada = f"{id} - {status} - {nova_descricao}\n"
                    tarefas[indice] = tarefa_atualizada  # Atualiza a tarefa na lista
                    # Reescreve todas as tarefas no arquivo
                    with open(self.arquivo, "w") as arquivo:
                        arquivo.writelines(tarefas)
                    return True
                else:
                    print("Tarefa não encontrada.")
                    return False
            else:
                print("Índice inválido.")
                return False
        except Exception as error:
            print(error.__class__.__name__)
            return False

    # Define o método concluirTarefa que recebe o índice da tarefa a ser concluída e o novo status como parâmetros
    def concluirTarefa(self,indice, novo_status):
        try:
            # Abre o arquivo em modo de leitura ("r")
            with open(self.arquivo, "r") as arquivo:
                # Lê todas as linhas do arquivo e armazena em uma lista
                tarefas = arquivo.readlines()
            # Verifica se o índice especificado é válido
            if indice >= 0 and indice < len(tarefas):
                # Extrai as partes da tarefa
                tarefa_parts = tarefas[indice].split(" - ", 2)
                if len(tarefa_parts) == 3:
                    _, status, _ = tarefa_parts
                    tarefa_parts[1] = novo_status  # Altera apenas o status
                    tarefas[indice] = " - ".join([tarefa_parts[0], tarefa_parts[1], tarefa_parts[2]])
                    # Reescreve todas as tarefas no arquivo
                    with open(self.arquivo, "w") as arquivo:
                        arquivo.writelines(tarefas)
                    return True
                else:
                    print("Tarefa não encontrada.")
                    return False
            else:
                print("Índice inválido.")
                return False
        except Exception as error:
            print(error.__class__.__name__)
            return False

    # Define o método adicionarTarefaConcluida que recebe a tarefa concluída como parâmetro
    def adicionarTarefaConcluida(self, tarefa_concluida):
        try:
            # Abre o arquivo em modo de anexação ("a")
            with open(self.arquivo, "a") as arquivo:
                # Escreve a tarefa concluída no arquivo
                arquivo.write(tarefa_concluida)
            return True
        except Exception as error:
            print(error.__class__.__name__)
            return False

    # Define o método listarTarefasConcluidas que não recebe nenhum parâmetro
    def listarTarefasConcluidas(self):
        try:
            # Abre o arquivo em modo de leitura ("r")
            with open(self.arquivo, "r") as arquivo:
                # Lê todas as linhas do arquivo e armazena em uma lista
                tarefas = arquivo.readlines()
            # Filtra as tarefas concluídas e armazena em uma nova lista
            tarefas_concluidas = [tarefa for tarefa in tarefas if "Concluída" in tarefa]
            return tarefas_concluidas
        except Exception as error:
            print(error.__class__.__name__)
            return False

            # Cria uma instância da classe Dao e atribui à variável DAO
DAO = Dao()
