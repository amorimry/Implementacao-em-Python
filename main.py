from classProduto import Produto
import utilsMercado

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

        novo_produto = {
        "Nome": nome,
        "Preço": preco,
        "Lote": lote,
        "Validade": validade,
        "Código": codigo,
        "Descrição": descricao
        }

        utilsMercado.produtos.append(novo_produto)

        Produto(nome, preco, lote, validade, codigo, descricao)

        print("""
    -- Produto cadastrado com sucesso!
""")
    elif op == "2":
        pass
    elif op == "3":
        pass
    elif op == "0":
        print("""
        -- Finalizando programa...
""")
        break
    else:
        print("Opção inválida, digite novamente.")

input("Digite Enter para fechar.")