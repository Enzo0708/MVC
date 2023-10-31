from Model import *  # Importa todas as classes do módulo Model
from Dao import *  # Importa todas as classes do módulo Dao
import random  # Importa o módulo random para gerar números aleatórios

class ControllerAdicionarTarefa:
    def __init__(self, tarefa):
        if not tarefa.strip():  # Verifica se a tarefa é vazia ou apenas espaços em branco
            print("Tarefa vazia. Não foi possível adicionar.")
        else:
            id = random.randint(1000, 9999) # Gera um número aleatório entre 1000 e 9999
            self.id = int(id)   # Converte o número gerado para inteiro
            self.status = "A fazer" # Define o status da tarefa como "A fazer"
            self.tarefa = tarefa    # Define a tarefa
            self.tarefa = f"{self.id} - {self.status} - {self.tarefa}\n"    # Define a tarefa no formato "id - status - tarefa"

            self.adicionar_tarefa() # Adiciona a tarefa

    def adicionar_tarefa(self): # Define o método adicionar_tarefa
        if DAO.AdicionarTarefa(self.tarefa):        # Correção: Chamada correta para DAO.AdicionarTarefa    
            print("Tarefa Adicionada")        # Correção: Mensagem de sucesso
        else:
            print("Não foi possível adicionar a tarefa.")     # Correção: Mensagem de erro


class ControllerExcluirTarefa:  # Define a classe ControllerExcluirTarefa
    def __init__(self, excluir):    # Define o método construtor que recebe o índice da tarefa a ser excluída como parâmetro
        try:
            self.excluir = int(excluir) # Converte o índice para inteiro
            self.excluir_tarefa()   # Exclui a tarefa
        except Exception as error:  # Se ocorrer um erro durante a execução do bloco de código dentro do try
            print(error.__class__.__name__) # Imprime o nome da classe do erro
            print("Não foi possível excluir a tarefa.") # Correção: Mensagem de erro

    def excluir_tarefa(self):   # Define o método excluir_tarefa
        tarefas = DAO.listarTarefas()   # Correção: Chamada correta para DAO.listarTarefas
        try:
            if self.excluir >= 1 and self.excluir <= len(tarefas):  # Verifica se o índice especificado é válido
                tarefa = tarefas[self.excluir - 1]  # Correção: Índice da lista começa em 0
                tarefa_parts = tarefa.split(" - ", 1)   # Extrai as partes da tarefa

                if len(tarefa_parts) > 1:   # Verifica se a tarefa foi encontrada
                    _, texto_tarefa = tarefa_parts  # Extrai as partes da tarefa
                    print(f"Excluindo a tarefa: {texto_tarefa}")    # Correção: Mensagem de sucesso

                    if DAO.excluirTarefa(self.excluir - 1):  # Correção: Chamada correta para DAO.ExcluirTarefa
                        print("Tarefa Excluída")    # Correção: Mensagem de sucesso
                    else:
                        print("Não foi possível excluir a tarefa. Verifique o índice.")
                else:
                    print("Tarefa não encontrada.")
            else:
                print("Índice inválido.")

        except Exception as error:
            print(error.__class__.__name__)
            


class ControllerListarTarefas:            
    #listar somente as tarefas que não foram concluidas
    def __init__(self):     
        self.lista = DAO.listarTarefas()    # Correção: Chamada correta para DAO.listarTarefas
        self.exibirTarefas()    # Exibe as tarefas

    def exibirTarefas(self):    # Define o método exibirTarefas
        if self.lista:  # Verifica se a lista não está vazia
            for i, tarefa in enumerate(self.lista, start=1):    # Correção: Índice da lista começa em 0
                tarefa_parts = tarefa.split(" - ", 2)   # Extrai as partes da tarefa
                if len(tarefa_parts) == 3:  # Verifica se a tarefa foi encontrada
                    _, status, texto_tarefa = tarefa_parts  # Extrai as partes da tarefa
                    if status == "A fazer": # Verifica se o status da tarefa é "A fazer"
                        print(f"[{i}] - Status: {status}, Tarefa: {texto_tarefa}")  # Correção: Índice da lista começa em 0
                else:   # Se a tarefa não foi encontrada
                    print(f"[{i}] - Tarefa não encontrada.")    # Correção: Índice da lista começa em 0


class ControllerConcluirTarefa: # Define a classe ControllerConcluirTarefa
    def __init__(self, indice, novo_status):    # Define o método construtor que recebe o índice da tarefa a ser concluída e o novo status como parâmetros
        try:
            self.indice = int(indice)   # Converte o índice para inteiro
            self.novo_status = novo_status  # Define o novo status
            self.concluirTarefa()   # Conclui a tarefa
        except Exception as error:  # Se ocorrer um erro durante a execução do bloco de código dentro do try
            print(error.__class__.__name__)
            print("Não foi possível concluir a tarefa.")
    def concluirTarefa(self):   # Define o método concluirTarefa
        try:    # Correção: Tratamento de exceção
            if self.indice > 0: # Verifica se o índice especificado é válido
                tarefas = DAO.listarTarefas()   # Correção: Chamada correta para DAO.listarTarefas

                if self.indice <= len(tarefas): # Verifica se o índice especificado é válido
                    if DAO.concluirTarefa(self.indice - 1, self.novo_status):   # Correção: Chamada correta para DAO.ConcluirTarefa
                        print("Tarefa alterada com sucesso.")   # Correção: Mensagem de sucesso
                    else:
                        print("Não foi possível alterar a tarefa.") 
                else:
                    print("Índice inválido.")
            else:
                print("Operação cancelada.")
        except Exception as error:
            print(error.__class__.__name__)
            print("Não foi possível concluir a tarefa.")


class ControllerListarTarefasConcluidas:    # Define a classe ControllerListarTarefasConcluidas
    #Lista somente as tarefas concluidas        
    def __init__(self):     
        self.lista = DAO.listarTarefas()    # Correção: Chamada correta para DAO.listarTarefas
        self.exibirTarefasConcluidas()  # Exibe as tarefas concluídas

    def exibirTarefasConcluidas(self):  # Define o método exibirTarefasConcluidas
        if self.lista:  # Verifica se a lista não está vazia
            for i, tarefa in enumerate(self.lista, start=1):    # Correção: Índice da lista começa em 0
                tarefa_parts = tarefa.split(" - ", 2)   # Extrai as partes da tarefa
                if len(tarefa_parts) == 3:  # Verifica se a tarefa foi encontrada
                    _, status, texto_tarefa = tarefa_parts  # Extrai as partes da tarefa
                    if status == "Concluído":   # Verifica se o status da tarefa é "Concluído"
                        print(f"[{i}] - Status: {status}, Tarefa: {texto_tarefa}")  # Correção: Índice da lista começa em 0
                else:   # Se a tarefa não foi encontrada
                    print(f"[{i}] - Tarefa não encontrada.")    # Correção: Índice da lista começa em 0


class ControllerAlterarTarefa:  # Define a classe ControllerAlterarTarefa
    def __init__(self, indice, nova_descricao): # Define o método construtor que recebe o índice da tarefa a ser alterada e a nova descrição como parâmetros
        try:
            if not nova_descricao.strip():  # Verifica se a tarefa é vazia ou apenas espaços em branco
                print("Tarefa vazia. Não foi possível adicionar.")  # Correção: Mensagem de erro
            else:   # Se a tarefa não for vazia
                self.indice = int(indice)   # Converte o índice para inteiro
                self.nova_descricao = nova_descricao    # Define a nova descrição
                self.alterar_tarefa()   # Altera a tarefa
        except Exception as error:      # Se ocorrer um erro durante a execução do bloco de código dentro do try
            print(error.__class__.__name__) 
            print("Não foi possível alterar a tarefa.")

    def alterar_tarefa(self):   # Define o método alterar_tarefa
        try:        # Correção: Tratamento de exceção
            if self.indice > 0: # Verifica se o índice especificado é válido
                tarefas = DAO.listarTarefas()   # Correção: Chamada correta para DAO.listarTarefas

                if self.indice <= len(tarefas): # Verifica se o índice especificado é válido
                    if DAO.alterarTarefa(self.indice - 1, self.nova_descricao):  # Correção: Chamada correta para DAO.AlterarTarefa
                        print("Tarefa alterada com sucesso.")
                    else:
                        print("Não foi possível alterar a tarefa.")
                else:
                    print("Índice inválido.")
            else:
                print("Operação cancelada.")
        except Exception as error:
            print(error.__class__.__name__)
            print("Não foi possível alterar a tarefa.")

