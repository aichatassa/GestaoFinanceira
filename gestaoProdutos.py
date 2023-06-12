from produto import Produto
class GestaoProdutos:
    def __init__(self, gestao_contabil):
        self.produtos = []
        self.gestao_contabil = gestao_contabil

    def cadastrar_produto(self, codigo, nome, preco):
        produto = Produto(codigo, nome, preco)
        self.produtos.append(produto)
        self.gestao_contabil.realizar_lancamento("01/01/2023", 12, preco)
        print("\n Produto cadastrado com sucesso! \n")

    def listar_produtos(self):
        if not self.produtos:
            print("\n Nenhum produto cadastrado. \n")
        else:
            for produto in self.produtos:
                print("------------------------------------------------------")
                print(f"Código: {produto.codigo}\tNome: {produto.nome}\tPreço: R${produto.preco:.2f}")
                print("------------------------------------------------------\n")

    def buscar_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                print("------------------------------------------------------")
                print(f"Código: {produto.codigo}\tNome: {produto.nome}\tPreço: R${produto.preco:.2f}")
                print("------------------------------------------------------\n")
                return
        print("Produto não encontrado.")

    def remover_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                self.produtos.remove(produto)
                print("--------------------------------")
                print("Produto removido com sucesso!")
                print("--------------------------------\n")
                return
        print("Produto não encontrado.")