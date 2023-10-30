from Model import *  # Importa todas as classes do módulo Model
from Dao import *  # Importa todas as classes do módulo Dao
import random  # Importa o módulo random para gerar números aleatórios

class ControllerAdicionarTarefa():  # Define a classe ControllerAdicionarTarefa
    def __init__(self, tarefa):  # Método construtor que recebe a tarefa como parâmetro
        id = random.randint(1000, 9999)  # Gera um número aleatório entre 1000 e 9999 para o ID da tarefa
        self.id = int(id)  # Converte o ID para inteiro
        self.status = "A fazer"  # Define o status da tarefa como "A fazer"
        self.tarefa = tarefa  # Atribui a tarefa passada como parâmetro para a instância atual
        self.tarefa = f"{self.id} - {self.status} - {self.tarefa} \n"  # Concatena o ID, o status e a tarefa em uma única string

        self.adicionar_tarefa()  # Chama o método adicionar_tarefa

    def adicionar_tarefa(self):  # Define o método adicionar_tarefa
        if DAO.AdicionarTarefa(self.tarefa):  # Correção: Chamada correta para DAO.AdicionarTarefa
            print("Tarefa Adicionada")  # Imprime uma mensagem de sucesso
        else:
            print("Não foi possível adicionar a tarefa.")
 


class ControllerExcluirTarefa:
    def __init__(self, excluir):
        self.excluir = int(excluir)
        self.excluir_tarefa()

    def excluir_tarefa(self):
        tarefas = DAO.listarTarefas()

        if self.excluir >= 1 and self.excluir <= len(tarefas):
            tarefa = tarefas[self.excluir - 1]
            tarefa_parts = tarefa.split(" - ", 1)

            if len(tarefa_parts) > 1:
                _, texto_tarefa = tarefa_parts
                print(f"Excluindo a tarefa: {texto_tarefa}")

                if DAO.excluirTarefa(self.excluir - 1):  # Correção: Chamada correta para DAO.ExcluirTarefa
                    print("Tarefa Excluída")
                else:
                    print("Não foi possível excluir a tarefa. Verifique o índice.")
            else:
                print("Tarefa não encontrada.")
        else:
            print("Índice inválido.")

class ControllerListarTarefas:
    def __init__(self):
        self.lista = DAO.listarTarefas()
        self.exibirTarefas()

    def exibirTarefas(self):
        if self.lista:
            for i, tarefa in enumerate(self.lista, start=1):
                tarefa_parts = tarefa.split(" - ", 2)  # Dividir em 3 partes

                if len(tarefa_parts) == 3:
                    _, status, texto_tarefa = tarefa_parts
                    print(f"[{i}] - Status: {status}, Tarefa: {texto_tarefa}")
                else:
                    print(f"[{i}] - Tarefa não encontrada.")

class ControllerConcluirTarefa:
    def __init__(self, concluir):
        self.concluir = int(concluir)
        self.concluir_tarefa()

    def concluir_tarefa(self):
        tarefas = DAO.listarTarefas()

        if self.concluir >= 1 and self.concluir <= len(tarefas):
            tarefa = tarefas[self.concluir - 1]
            tarefa_parts = tarefa.split(" - ", 1)

            if len(tarefa_parts) > 1:
                _, texto_tarefa = tarefa_parts
                print(f"Concluindo a tarefa: {texto_tarefa}")

                if DAO.concluirTarefa(self.concluir - 1):
                    print("Tarefa Concluída")
                    # Agora, adicione a tarefa concluída à lista de tarefas concluídas
                    tarefa_concluida = f"{texto_tarefa} - Concluída"  # Adiciona o status de concluída
                    if DAO.adicionarTarefaConcluida(tarefa_concluida):
                        print("Tarefa adicionada à lista de tarefas concluídas")
                    else:
                        print("Não foi possível adicionar a tarefa à lista de tarefas concluídas.")
                else:
                    print("Não foi possível concluir a tarefa. Verifique o índice.")
            else:
                print("Tarefa não encontrada.")
        else:
            print("Índice inválido.")


class ControllerListarTarefasConcluidas:
    def __init__(self):
        self.lista = DAO.listarTarefasConcluidas()
        self.exibirTarefas()

    def exibirTarefas(self):
        if self.lista:
            for i, tarefa in enumerate(self.lista, start=1):
                tarefa_parts = tarefa.split(" - ", 3)  # Correção: Dividir em 4 partes

                if len(tarefa_parts) == 4:  # Correção: Verificar se há 4 partes
                    _, status, texto_tarefa, _ = tarefa_parts  # Correção: Adicionar uma variável para o último valor não usado
                    print(f"[{i}] - Status: {status}, Tarefa: {texto_tarefa}")
                else:
                    print(f"[{i}] - Tarefa não encontrada.")


class ControllerAlterarTarefa:
    def __init__(self, indice, nova_descricao):
        self.indice = int(indice)
        self.nova_descricao = nova_descricao
        self.alterar_tarefa()

    def alterar_tarefa(self):
        if self.indice > 0:
            tarefas = DAO.listarTarefas()

            if self.indice <= len(tarefas):
                if DAO.alterarTarefa(self.indice - 1, self.nova_descricao):
                    print("Tarefa alterada com sucesso.")
                else:
                    print("Não foi possível alterar a tarefa.")
            else:
                print("Índice inválido.")
        else:
            print("Operação cancelada.")