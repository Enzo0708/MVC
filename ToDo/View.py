from Controller import *  # Importa todas as classes do módulo Controller
import os  # Importa o módulo os que fornece funções para interagir com o sistema operacional

sair = 0  # Inicializa a variável sair com 0

while sair == 0:  # Inicia um loop que só será interrompido quando a variável sair for diferente de 0
    
    os.system("cls")  # Limpa a tela do console
    
    # Imprime o menu do programa
    print("    SOFTWARE DE TO-DO")
    print(" ________________________")
    print("|[1] -> ADICIONAR TAREFA |")
    print("|[2] -> LISTAR TAREFAS   |")
    print("|[3] -> ALTERAR TAREFA   |")
    print("|[4] -> CONCLUIR TAREFA  |")
    print("|[5] -> LISTAR CONCLUIDAS|")
    print("|[6] -> EXCLUIR TAREFA   |")
    print("|[7] -> SAIR             |")
    print("|________________________|")
    print("")

    menu = input("-> ")  # Recebe a opção do usuário
    
    match menu:  # Verifica qual opção foi escolhida
        
        case "1":  # Se a opção escolhida foi "1"
            os.system("cls")  # Limpa a tela do console
            tarefa = input("Adicione uma TAREFA -> ")  # Recebe a tarefa do usuário
            adicionarTarefa = ControllerAdicionarTarefa(tarefa)  # Adiciona a tarefa
            os.system("pause")  # Pausa a execução do programa até que o usuário pressione qualquer tecla

        case "2":  # Se a opção escolhida foi "2"
            os.system("cls")  # Limpa a tela do console
            listarTarefas = ControllerListarTarefas()  # Lista as tarefas
            os.system("pause")  # Pausa a execução do programa até que o usuário pressione qualquer tecla

        case "3":  # Se a opção escolhida foi "3"
            os.system("cls")  # Limpa a tela do console
            listarTarefas = ControllerListarTarefas()  # Lista as tarefas
            indice = input("Qual o indice da tarefa que deseja alterar?\n-> ")  # Recebe o índice da tarefa que o usuário deseja alterar
            nova_descricao = input("Qual a nova descrição da tarefa?\n-> ")  # Recebe a nova descrição da tarefa
            alterarTarefa = ControllerAlterarTarefa(indice, nova_descricao)  # Altera a tarefa
            os.system("pause")

        case "4":  # Se a opção escolhida foi "4"
            os.system("cls")  # Limpa a tela do console
            listarTarefas = ControllerListarTarefas()  # Lista as tarefas
            concluir = input("Qual o índice da tarefa que deseja concluir?\n-> ")  # Recebe o índice da tarefa que o usuário deseja concluir
            try:
                concluir = int(concluir)
                concluirTarefa = ControllerConcluirTarefa(concluir)  # Conclui a tarefa
            except ValueError:
                print("Índice inválido. Certifique-se de inserir um número válido.")
            os.system("pause")

        case "5":  # Se a opção escolhida foi "5"
            os.system("cls")  # Limpa a tela do console
            listarTarefas = ControllerConcluirTarefa(1)  # Supondo que o índice da tarefa que deseja concluir seja 1
            os.system("pause")

        case "6":  # Se a opção escolhida foi "6"
            os.system("cls")  # Limpa a tela do console
            listarTarefas = ControllerListarTarefas()  # Lista as tarefas
            excluir = input("Qual o indice da tarefa que deseja excluir?\n-> ")  # Recebe o índice da tarefa que o usuário deseja excluir
            excluirTarefa = ControllerExcluirTarefa(excluir)  # Exclui a tarefa
            print("\nLista:")
            listarTarefas = ControllerListarTarefas()  # Lista as tarefas novamente
            os.system("pause")  # Pausa a execução do programa até que o usuário pressione qualquer tecla
        case "7":  # Se a opção escolhida foi "7"
            sair = 1  # Altera o valor da variável sair para 1, interrompendo o loop