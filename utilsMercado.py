def exibir_produto(lista):
    for i, produto in enumerate(lista):
        print(f"{i+1}. {produto.nome}\n")