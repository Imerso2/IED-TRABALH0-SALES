pessoas = []

def adicionar():
    nome = input("digite seu nome")
    idade = input("digite sua idade")
    cidade = input("qual é a sua cidade?")
    pessoa = {"nome": nome, "idade": idade, "cidade": cidade}
    pessoas.append(pessoa)

while True:
    tem_transporte = input("\n você tem um transporte? (sim/não): ").lower()
    
    if tem_transporte == "não":
        print("serviço inelegivel")
        break
    elif tem_transporte == "sim":
        adicionar()
    else:
        print("opção inválida")
    print(pessoas)
    break

