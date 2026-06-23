produtos = []

print("""
        -- Mini Mercado Bom Preço --
Olá, bem vindo ao sistema do mercado.""")

while True:
    print("""
        - MENU DE OPÇÕES -
    1. Cadastrar produto no sistema
        
    0. Finalizar sistema
    """)
    op = input("Digite a opção desejada: ")
    if op == "1":
        print("""
    1. CADASTRAR PRODUTO NO SISTEMA
""")
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        lote = input("Digite o código do lote do produto: ")
        validade = input("Digite a validade do produto (00/00/0000): ")
        codigo = input("Digite o código de barras do produto: ")
        descricao = input("Digite uma descrição do produto: ")

        novo_produto = {
            "Nome"
        }

    elif op == "0":
        break
    else:
        print("Número inválido, digite novamente.")