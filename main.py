from classProduto import Produto
import utilsMercado

produtos = [
    Produto(
        nome="Arroz Integral",
        preco=24.90,
        lote=1024,
        validade="12/12/2027",
        codigo="ARZ-001",
        descricao="Pacote de arroz integral tipo 1 de 5kg."),
    Produto(
        nome="Feijão Preto",
        preco=8.50,
        lote=2048,
        validade="05/10/2026",
        codigo="FJN-002",
        descricao="Feijão preto selecionado em pacote de 1kg."),
    Produto(
        nome="Azeite de Oliva Extra Virgem",
        preco=42.00,
        lote=512,
        validade="20/03/2028",
        codigo="AZE-003",
        descricao="Garrafa de azeite extra virgem acidez máxima 0.5%."),
    Produto(
        nome="Café Torrado e Moído",
        preco=18.25,
        lote=4096,
        validade="15/01/2027",
        codigo="CAF-004",
        descricao="Café a vácuo com torra média de 500g."),
    Produto(
        nome="Leite Integral UHT",
        preco=5.49,
        lote=128,
        validade="01/09/2026",
        codigo="LTE-005",
        descricao="Caixa de leite integral de 1 litro.")
]


print("""
        == Bem vindo ao sistema de cadastro do Mini Mercado Bom Preço ==
""")

while True:
    print("""
    -- Menu de opções --
1. Cadastrar produto
2. Ver lista de produtos
3. ver informações de um produto
      
0. Finalizar sistema
""")
    op = input("Digite sua opção: ")
    if op == "1":
        print("""
    -- CASDATRAR PRODUTO --
""")
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        lote = int(input("Digite a quantidade de lotes: "))
        validade = input("Digite a validade do lote do protudo: ")
        codigo = input("Digite o código do produto: ")
        descricao = input("Digite uma descrição sobre esse produto: ")

        produto_objeto = Produto(nome, preco, lote, validade, codigo, descricao)

        produtos.append(produto_objeto)

        print("""
    -- Produto cadastrado com sucesso!
""")
        
        input("Digite Enter para voltar ao menu.")
    elif op == "2":
        print("""
    -- LISTA DOS PRODUTOS --
""")
        utilsMercado.exibir_produto(produtos)

        input("Digite Enter para voltar ao menu.")
    elif op == "3":
        print("""
    -- INFORMAÇÕES DO PRODUTO --
""")
        utilsMercado.exibir_produto(produtos)
        op_produto = int(input("Digite o número do produto que você deseja ver informações: "))
        indice_ajustado = op_produto - 1
        produto_escolhido = produtos[indice_ajustado]
        produto_escolhido.vizualizar_produto()

        input("Digite Enter para voltar ao menu.")
    elif op == "0":
        print("""
        -- Finalizando programa...
""")
        break
    else:
        print("Opção inválida, digite novamente.")

input("Digite Enter para fechar.")