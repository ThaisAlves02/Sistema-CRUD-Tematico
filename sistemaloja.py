# Lista que armazena os elementos
loja_informatica = [
    {"nome": "Notebook", "preço": 3500.00, "quantidade": 10},
    {"nome": "Smartphone", "preço": 1999.90, "quantidade": 25},
    {"nome": "Monitor 24", "preço": 850.00, "quantidade": 15},
    {"nome": "Teclado Mecânico", "preço": 299.90, "quantidade": 40},
    {"nome": "Mouse Gamer", "preço": 150.00, "quantidade": 50},
    {"nome": "Fone de Ouvido Bluetooth", "preço": 199.00, "quantidade": 30},
    {"nome": "Cadeira Ergonômica", "preço": 1200.00, "quantidade": 8},
    {"nome": "Webcam Full HD", "preço": 349.90, "quantidade": 12},
    {"nome": "Roteador Wi-Fi 6", "preço": 450.00, "quantidade": 20},
    {"nome": "SSD 1TB NVMe", "preço": 420.00, "quantidade": 18}

    ]

# ---- Operações CRUD ----
def cadastrar_produto():
    print("CADASTRAR PRODUTOS")
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = input("Digite o preço do produto: ")
    qtd_produto = input("Digite a quantidade do produto: ")

    novo_produto = {
        "nome": nome_produto,
        "preço": preco_produto,
        "quantidade": qtd_produto
    }

    loja_informatica.append(novo_produto)


def ver_produto():
    print("VISUALIZAR PRODUTOS")
    for i, produto in enumerate(loja_informatica):
        print(f"{i+1}. {produto["nome"]} | {produto["preço"]} | {produto["quantidade"]}")


def alterar_produto():
    ver_produto()

    num = int(input("Digite o número do produto que deseja remover: "))

    produto_escolhido = loja_informatica[num - 1]

    novo_nome = input(f"Digite o novo nome ({produto_escolhido["nome"]}): ")
    if novo_nome:
        produto_escolhido["nome"] = novo_nome


    novo_preco = input("Digite o novo preço : ")
    if novo_preco:
        produto_escolhido["preço"] = novo_preco

    nova_qtd = input("Digite a nova quantidade: ")
    if nova_qtd:
        produto_escolhido["quantidade"] = nova_qtd

    print(f"""
        INFORMAÇÕES DO PRODUTO:
            
        NOME: {produto_escolhido["nome"]}
        PREÇO: R${produto_escolhido['preço']}
        QUANTIDADE: {produto_escolhido['quantidade']}
            """)
            
def remover_produto():
      ver_produto()
      
      num = int(input ("Digite o número do produto que você deseja remover: "))
      
      produto_escolhido = loja_informatica.pop(num - 1) 
      
      print(f"PRODUTO REMOVIDO COM SUCESSO!")
      
def menu_principal():
    while True:

        print(f"""
BEM VINDO AO SISTEMA DA NOSSA LOJA!
          
Menu:
          
          1. Cadastrar produto
          2. Ver produto
          3. Alterar produto
          4. Remover produto

          0. Sair
""")

        op = input("Digite a opção desejada:")

        if op == "1":
            cadastrar_produto()

        elif op == "2":
            ver_produto()

        elif op == "3":
            alterar_produto()

        elif op == "4":
            remover_produto()

        elif op == "0":
            print("SAINDO DO PROGRAMA...")
            break

        else:
            print("DIGITE A OPÇÃO NOVAMENTE")

        input("TECLE ENTER PARA CONTINUAR")


menu_principal()