tarefas = []            # Cria uma lista vazia chamada 'tarefas' (para guardar as tarefas ativas)
historico = []          # Cria uma lista vazia chamada 'historico' (para guardar a ordem das tarefas)
fila_execucao = []      # Cria uma lista vazia chamada 'fila_execucao' (para manter a fila de execução)

def salvar_em_arquivo():  # Define a função que salva as tarefas no arquivo .txt
    with open("tarefas.txt", "w", encoding="utf-8") as arquivo:  # 'open' abre o arquivo em modo escrita ('w'); 'with' fecha automático
        for t in tarefas:  # Para cada tarefa na lista 'tarefas'
            arquivo.write(t + "\n")  # Escreve a tarefa no arquivo, com quebra de linha

def adicionar_tarefa(tarefa):  # 'def' define uma função chamada 'adicionar_tarefa' que recebe o parâmetro 'tarefa'
    tarefas.append(tarefa)     # '.append()' adiciona a tarefa no final da lista 'tarefas'
    historico.append(tarefa)   # Adiciona a mesma tarefa no final da lista 'historico'
    fila_execucao.append(tarefa)  # Adiciona a tarefa também no final da fila de execução
    salvar_em_arquivo()       # Chama a função para salvar as tarefas no arquivo
    print(f"Tarefa '{tarefa}' adicionada!\n")  # 'print()' exibe uma mensagem formatada na tela com o nome da tarefa

def desfazer_ultima_tarefa():  # Define a função 'desfazer_ultima_tarefa' sem parâmetros
    if historico:              # 'if' verifica se a lista 'historico' não está vazia
        ultima = historico.pop()         # '.pop()' remove e retorna o último item da lista 'historico', e guarda em 'ultima'
        tarefas.remove(ultima)          # '.remove()' retira a tarefa da lista 'tarefas'
        fila_execucao.remove(ultima)    # Também retira a tarefa da fila de execução
        salvar_em_arquivo()             # Salva a lista atualizada no arquivo
        print(f"Tarefa '{ultima}' desfeita!\n")  # Mostra na tela que essa tarefa foi desfeita
    else:
        print("Nenhuma tarefa para desfazer.\n")  # Se não houver tarefas, mostra essa mensagem

def atender_tarefa():  # Define a função 'atender_tarefa' sem parâmetros
    if fila_execucao:  # Verifica se a lista 'fila_execucao' não está vazia
        feita = fila_execucao.pop(0)  # '.pop(0)' remove e retorna o primeiro item da lista (modo fila)
        tarefas.remove(feita)         # Remove a tarefa correspondente da lista 'tarefas'
        salvar_em_arquivo()           # Salva a lista atualizada no arquivo
        print(f"Tarefa '{feita}' atendida!\n")  # Mostra que a tarefa foi atendida
    else:
        print("Nenhuma tarefa para atender.\n")  # Caso não haja tarefas, avisa o usuário

def mostrar_tarefas():  # Define a função 'mostrar_tarefas' sem parâmetros
    print("\n📋 Lista de Tarefas:")  # Exibe um título no console
    for i, t in enumerate(tarefas):  # 'for' percorre a lista 'tarefas', 'enumerate' dá o índice (i) e o valor (t)
        print(f"{i + 1}. {t}")       # Exibe a tarefa com seu número (índice + 1)
    print()  # Exibe uma linha em branco para separar

while True:  # 'while True' cria um laço infinito que só vai parar com um 'break'
    print("1. Adicionar Tarefa")            # Exibe a opção 1 no menu
    print("2. Desfazer Última Tarefa")      # Exibe a opção 2
    print("3. Atender Tarefa (modo fila)")  # Exibe a opção 3
    print("4. Mostrar Tarefas")             # Exibe a opção 4
    print("5. Sair")                        # Exibe a opção 5

    opcao = input("Escolha uma opção: ")  # 'input()' lê um valor digitado pelo usuário e guarda em 'opcao' como string

    if opcao == '1':  # Verifica se o valor digitado foi '1'
        tarefa = input("Digite a tarefa: ")  # Lê do usuário o texto da tarefa
        prioridade = input("Digite a prioridade ou data (ex: Alta / 10/05): ")  # Lê a prioridade ou data da tarefa
        texto_final = f"{tarefa} [Prioridade/Data: {prioridade}]"  # Junta a tarefa com a prioridade entre colchetes
        adicionar_tarefa(texto_final)  # Chama a função 'adicionar_tarefa', passando o texto completo

    elif opcao == '2':  # Verifica se o valor digitado foi '2'
        desfazer_ultima_tarefa()  # Chama a função que desfaz a última tarefa

    elif opcao == '3':  # Verifica se o valor digitado foi '3'
        atender_tarefa()  # Chama a função que atende (executa) a próxima tarefa da fila

    elif opcao == '4':  # Verifica se o valor digitado foi '4'
        mostrar_tarefas()  # Chama a função que mostra as tarefas atuais

    elif opcao == '5':  # Verifica se o valor digitado foi '5'
        print("Saindo do programa...")  # Exibe mensagem de encerramento
        break  # 'break' termina o laço 'while' e encerra o programa

    else:  # Se o valor digitado não for 1, 2, 3, 4 ou 5
        print("Opção inválida!\n")  # Exibe mensagem de erro