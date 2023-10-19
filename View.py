from Controller import *
import os

sair = 0
while sair == 0:
    os.system("cls")
    print("    SOFTWARE DE TO-DO")
    print(" ________________________")
    print("|[1] -> ADICIONAR TAREFA |")
    print("|[2] -> LISTAR TAREFAS   |")
    print("|[3] -> EXCLUIR TAREFAS  |")
    print("|[4] -> SAIR             |")
    print("|________________________|")
    print("")

    #Convertendo o input para inteiro

    menu = input("-> ")
    
    
    match menu:
        case "1":
            os.system("cls")
            tarefa = input("Adicione uma TAREFA -> ")
            adicionarTarefa = ControllerAdicionarTarefa(tarefa)
            os.system("pause")
        case "2":
            os.system("cls")
            listarTarefas = ControllerListarTarefas()
            os.system("pause")
        case "3":
            os.system("cls")
            listarTarefas = ControllerListarTarefas()
            excluir = input("Qual o indice da tarefa que deseja excluir?\n-> ")
            excluirTarefa = ControllerExcluirTarefa(excluir)
            print("\nLista:")
            listarTarefas = ControllerListarTarefas()
            os.system("pause")
        case "4":
            sair = 1
            print("Saindo...")
            os.system("pause")
        case _:
            print("Opção Invalida")
            os.system("pause")