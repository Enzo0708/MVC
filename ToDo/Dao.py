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
        

    def listarTarefas(self):  # Define o método listar Tarefas que não recebe nenhum parâmetro
        try:  # Tenta executar o bloco de código dentro do try
            with open(self.arquivo, "r") as arquivo:  # Abre o arquivo em modo de leitura ("r")
                return arquivo.readlines()  # Retorna uma lista contendo todas as linhas do arquivo

        except Exception as error:  # Se ocorrer um erro durante a execução do bloco de código dentro do try
            print(error.__class__.__name__)  # Imprime o nome da classe do erro
            return False  # Retorna False indicando que as tarefas não foram listadas com sucesso


    def excluirTarefa(self, excluir):
        try:
            with open(self.arquivo, "r") as arquivo:
                tarefas = arquivo.readlines()
                tarefas.pop(excluir)

            with open(self.arquivo, "w") as arquivo:
                for tarefa in tarefas:
                    arquivo.write(tarefa)

            return True

        except Exception as error:
            print(error.__class__.__name__)
            return False
            

    def alterarTarefa(self, indice, nova_descricao):
        try:
            with open(self.arquivo, "r") as arquivo:
                tarefas = arquivo.readlines()
            
            if indice >= 0 and indice < len(tarefas):
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

        
    def concluirTarefa(self,indice, novo_status):
        try:
            with open(self.arquivo, "r") as arquivo:
                tarefas = arquivo.readlines()

            if indice >= 0 and indice < len(tarefas):
                tarefa_parts = tarefas[indice].split(" - ", 2)
                if len(tarefa_parts) == 3:
                    _, status, _ = tarefa_parts
                    tarefa_parts[1] = novo_status  # Altera apenas o status
                    tarefas[indice] = " - ".join([tarefa_parts[0], tarefa_parts[1], tarefa_parts[2]])

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


    def adicionarTarefaConcluida(self, tarefa_concluida):
        try:
            with open(self.arquivo, "a") as arquivo:
                arquivo.write(tarefa_concluida)

            return True

        except Exception as error:
            print(error.__class__.__name__)
            return False


    def adicionarTarefaConcluida(self, tarefa_concluida):
        try:
            with open(self.arquivo, "a") as arquivo:
                arquivo.write(tarefa_concluida)

            return True

        except Exception as error:
            print(error.__class__.__name__)
            return False


    def listarTarefasConcluidas(self):
        try:
            with open(self.arquivo, "r") as arquivo:
                tarefas = arquivo.readlines()

            tarefas_concluidas = [tarefa for tarefa in tarefas if "Concluída" in tarefa]

            return tarefas_concluidas

        except Exception as error:
            print(error.__class__.__name__)
            return False


DAO = Dao()  # Cria uma instância da classe Dao e atribui à variável DAO