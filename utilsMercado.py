produtos = []

def exibir_produto(lista):
    for i, produto in enumerate(lista):
        print(f"""
    -- Lista dos produtos da loja""")
        print(f"""{i+1}. {produto["Nome"]}
""")