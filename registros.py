import json
import readline  #para histórico de input no terminal
from datetime import datetime



try:
    #tenta abrir o arquivo de registros existentes
    with open("registros.json", "r", encoding="utf-8") as f:
        registros = json.load(f)
except FileNotFoundError:
    #se não existir, cria uma lista vazia
    registros = []

#funcoes

def listar():
    #Mostra todos os registros salvos
    if not registros:
        print("Nenhum registro encontrado!")
        return
    for i, bloco in enumerate(registros, start=1):
        print("―" * 50)
        print(f"{i} -\n{bloco}")
        print("―" * 50)
        print("\n\n")


def registar():
    """Permite ao usuário criar um novo registro"""
    print("Digite aqui (ou 'sair' para terminar):\n")

    bloco = []
    while True:
        linha = input(" | ")
        if linha.lower() == "sair":
            break
        bloco.append(linha)

    bloco_tex = "\n".join(bloco)
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
    bloco_data = f"[{data_hora}]\n{bloco_tex}"

    registros.append(bloco_data)

    #salva no arquivo JSON
    with open("registros.json", "w", encoding="utf-8") as f:
        json.dump(registros, f, ensure_ascii=False, indent=4)


def remover():
    """Permite remover um registro pelo número"""
    listar()
    if not registros:
        return
    try:
        escolha = int(input("Digite o número do registro que deseja apagar: "))
    except ValueError:
        print("Digite um número válido!")
        return

    if 0 < escolha <= len(registros):
        bloco_rem = registros.pop(escolha - 1)
        #atualiza o arquivo JSON
        with open("registros.json", "w", encoding="utf-8") as f:
            json.dump(registros, f, ensure_ascii=False, indent=4)
        print("\nBloco removido com sucesso!")
        input("\nAperte 'enter' para sair \n")
    else:
        print("Número inválido")




livro = r"""
░▒▓███████▓▒░░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓███████▓▒░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓███████▓▒░░▒▓██████▓▒░░▒▓█▓▒▒▓███▓▒░▒▓█▓▒░░▒▓██████▓▒░   ░▒▓█▓▒░   ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░  
"""

#menu

while True:
    print("■" * 110)
    print(livro)
    print("1 → Anotar")
    print("2 → Ver")
    print("3 → Remover")
    print("4 → Sair")

    opcao = input("\nDigite sua opção: ")
    print("■" * 110)

    if opcao == "1":
        registar()
    elif opcao == "2":
        listar()
        input("\nAperte 'enter' para voltar ao menu: ")
    elif opcao == "3":
        remover()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Tente novamente.")
