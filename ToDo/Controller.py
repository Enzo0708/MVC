from Model import *  # Importa todas as classes do módulo Model
from Dao import *  # Importa todas as classes do módulo Dao
import random  # Importa o módulo random para gerar números aleatórios

class ControllerAdicionarTarefa:
    def __init__(self, tarefa):
        if not tarefa.strip():  # Verifica se a tarefa é vazia ou apenas espaços em branco
            print("Tarefa vazia. Não foi possível adicionar.")
        else:
            id = random.randint(1000, 9999)
            self.id = int(id)
            self.status = "A fazer"
            self.tarefa = tarefa
            self.tarefa = f"{self.id} - {self.status} - {self.tarefa}\n"

            self.adicionar_tarefa()

    def adicionar_tarefa(self):
        if DAO.AdicionarTarefa(self.tarefa):
            print("Tarefa Adicionada")
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
    #listar somente as tarefas que não foram concluidas
    def __init__(self):
        self.lista = DAO.listarTarefas()
        self.exibirTarefas()

    def exibirTarefas(self):
        if self.lista:
            for i, tarefa in enumerate(self.lista, start=1):
                tarefa_parts = tarefa.split(" - ", 2)
                if len(tarefa_parts) == 3:
                    _, status, texto_tarefa = tarefa_parts
                    if status == "A fazer":
                        print(f"[{i}] - Status: {status}, Tarefa: {texto_tarefa}")
                else:
                    print(f"[{i}] - Tarefa não encontrada.")


class ControllerConcluirTarefa:
    def __init__(self, indice, novo_status):
        self.indice = int(indice)
        self.novo_status = novo_status
        self.concluirTarefa()

    def concluirTarefa(self):
        if self.indice > 0:
            tarefas = DAO.listarTarefas()

            if self.indice <= len(tarefas):
                if DAO.concluirTarefa(self.indice - 1, self.novo_status):
                    print("Tarefa alterada com sucesso.")
                else:
                    print("Não foi possível alterar a tarefa.")
            else:
                print("Índice inválido.")
        else:
            print("Operação cancelada.")


class ControllerListarTarefasConcluidas:
    #Lista somente as tarefas concluidas    
    def __init__(self):
        self.lista = DAO.listarTarefas()
        self.exibirTarefasConcluidas()

    def exibirTarefasConcluidas(self):
        if self.lista:
            for i, tarefa in enumerate(self.lista, start=1):
                tarefa_parts = tarefa.split(" - ", 2)
                if len(tarefa_parts) == 3:
                    _, status, texto_tarefa = tarefa_parts
                    if status == "Concluído":
                        print(f"[{i}] - Status: {status}, Tarefa: {texto_tarefa}")
                else:
                    print(f"[{i}] - Tarefa não encontrada.")


class ControllerAlterarTarefa:
    def __init__(self, indice, nova_descricao):
        if not nova_descricao.strip():  # Verifica se a tarefa é vazia ou apenas espaços em branco
            print("Tarefa vazia. Não foi possível adicionar.")
        else:
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

