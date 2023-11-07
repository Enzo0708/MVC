import os
class Dao:
    def __init__(self):
        self.arquivo = "tarefas.txt"
        if not os.path.isfile(self.arquivo) or os.path.getsize(self.arquivo) == 0:
            # Se o arquivo não existir ou estiver vazio, adicione o cabeçalho
            with open(self.arquivo, "w") as arquivo:
                arquivo.write("ID   -   STATUS   - TAREFA\n")


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
        try:
            with open(self.arquivo, "r") as arquivo:
                return arquivo.readlines()
        except Exception as error:
            print(error.__class__.__name__)
            return False
        
    # Define o método excluirTarefa que recebe o índice da tarefa a ser excluída como parâmetro
    def excluirTarefa(self,indice, novo_status):
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

    # Define o método alterarTarefa que recebe o índice da tarefa a ser alterada e a nova descrição como parâmetros
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
        except Exception as error:
            print(error.__class__.__name__)
            return False

    def concluirTarefa(self, indice, novo_status):
        try:
            tarefas = self.listarTarefas()
            if indice >= 0 and indice < len(tarefas):
                tarefa_parts = tarefas[indice].split(" - ", 2)
                if len(tarefa_parts) == 3:
                    tarefa_parts[1] = novo_status
                    tarefas[indice] = " - ".join(tarefa_parts)
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

    def listarTarefasConcluidas(self):
        try:
            # Abre o arquivo em modo de leitura ("r")
            with open(self.arquivo, "r") as arquivo:
                # Lê todas as linhas do arquivo e armazena em uma lista
                tarefas = arquivo.readlines()
            # Filtra as tarefas concluídas e armazena em uma nova lista
            tarefas_concluidas = [tarefa for tarefa in tarefas if "C" in tarefa]
            return tarefas_concluidas
        except Exception as error:
            print(error.__class__.__name__)
            return False
    

DAO = Dao()
