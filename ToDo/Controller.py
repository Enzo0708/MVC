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
            self.status = "A" # Define o status da tarefa como "A fazer"
            self.tarefa = tarefa    # Define a tarefa
            self.tarefa = f"{self.id} - {self.status} - {self.tarefa}\n"    # Define a tarefa no formato "id - status - tarefa"

            self.adicionar_tarefa() # Adiciona a tarefa

    def adicionar_tarefa(self): # Define o método adicionar_tarefa
        if DAO.AdicionarTarefa(self.tarefa):        # Correção: Chamada correta para DAO.AdicionarTarefa    
            print("Tarefa Adicionada")        # Correção: Mensagem de sucesso
        else:
            print("Não foi possível adicionar a tarefa.")     # Correção: Mensagem de erro


class ControllerExcluirTarefa:  # Define a classe ControllerExcluirTarefa
    def __init__(self, indice, novo_status):    # Define o método construtor que recebe o índice da tarefa a ser concluída e o novo status como parâmetros
        try:
            self.indice = int(indice)   # Converte o índice para inteiro
            self.novo_status = novo_status  # Define o novo status
            self.concluirTarefa()   # Conclui a tarefa
        except Exception as error:  # Se ocorrer um erro durante a execução do bloco de código dentro do try
            print(error.__class__.__name__)
            print("Não foi possível concluir a tarefa.")
    def excluirTarefa(self):   # Define o método concluirTarefa
        try:    # Correção: Tratamento de exceção
            if self.indice > 0: # Verifica se o índice especificado é válido
                tarefas = DAO.listarTarefas()   # Correção: Chamada correta para DAO.listarTarefas

                if self.indice <= len(tarefas): # Verifica se o índice especificado é válido
                    if DAO.concluirTarefa(self.indice, self.novo_status):   # Correção: Chamada correta para DAO.ConcluirTarefa
                        print("Tarefa excluida com sucesso.")   # Correção: Mensagem de sucesso
                    else:
                        print("Não foi possível alterar a tarefa.") 
                else:
                    print("Índice inválido.")
            else:
                print("Operação cancelada.")
        except Exception as error:
            print(error.__class__.__name__)
            print("Não foi possível concluir a tarefa.")


class ControllerListarTarefas:
    def __init__(self):
        self.lista = DAO.listarTarefas()
        self.exibirTarefas()

    def exibirTarefas(self):
        if self.lista:
            i = 1
            for tarefa in self.lista:
                tarefa_parts = tarefa.split(" - ", 2)
                if len(tarefa_parts) == 3:
                    _, status, texto_tarefa = tarefa_parts
                    if status == "A":
                        print(f"[{i}] - Status: {status}, Tarefa: {texto_tarefa}")
                        i += 1  # Incrementa o índice a cada tarefa válida
                else:
                    print(f"[{i}] - Tarefa não encontrada.")
                    i += 1  # Incrementa o índice, mesmo que a tarefa não seja encontrad


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
                    if DAO.concluirTarefa(self.indice, self.novo_status):   # Correção: Chamada correta para DAO.ConcluirTarefa
                        print("Tarefa concluida com sucesso.")   # Correção: Mensagem de sucesso
                    else:
                        print("Não foi possível concluir a tarefa.") 
                else:
                    print("Índice inválido.")
            else:
                print("Operação cancelada.")
        except Exception as error:
            print(error.__class__.__name__)
            print("Não foi possível concluir a tarefa.")
    

class ControllerListarTarefasConcluidas:
    def __init__(self):
        self.lista = DAO.listarTarefasConcluidas()
        self.exibirTarefasConcluidas()

    def exibirTarefasConcluidas(self):
        if self.lista:
            i = 1
            for tarefa in self.lista:
                tarefa_parts = tarefa.split(" - ", 2)
                if len(tarefa_parts) == 3:
                    _, status, texto_tarefa = tarefa_parts
                    if status == "C":
                        print(f"[{i}] - Status: {status}, Tarefa: {texto_tarefa}")
                        i += 1  # Incrementa o índice a cada tarefa válida
                else:
                    print(f"[{i}] - Tarefa não encontrada.")
                    i += 1  # Incrementa o índice, mesmo que a tarefa não seja encontrada




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
                    if DAO.alterarTarefa(self.indice, self.nova_descricao):  # Correção: Chamada correta para DAO.AlterarTarefa
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
