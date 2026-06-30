class Produto():
    def __init__(self, nome, preco, lote, validade, codigo, descricao):
        self.nome = nome
        self.preco = preco
        self.lote = lote
        self.validade = validade
        self.codigo = codigo
        self.descricao = descricao

    def vizualizar_produto(self):
        print(f"""
    -- Vizualizando produto escolhido --
        
    Nome: {self.nome}
    Preço: R$ {self.preco:.2f}
    Lote: {self.lote}
    Validade: {self.validade}
    Código: {self.codigo}
    Descrição: {self.descricao}
""")