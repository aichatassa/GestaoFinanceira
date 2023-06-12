from conta import Conta
from gestaoContabil import GestaoContabil
from gestaoProdutos import GestaoProdutos

# Criando as contas contábeis
contas = [
    Conta(1, "Caixa", "ATIVO"),
    Conta(2, "Conta Bancária", "ATIVO"),
    Conta(3, "Contas a Receber", "ATIVO"),
    Conta(4, "Estoque", "ATIVO"),
    Conta(5, "Bens", "ATIVO"),
    Conta(6, "Contas a Pagar", "PASSIVO"),
    Conta(7, "Capital Social", "PASSIVO"),
    Conta(8, "Resultados", "PASSIVO"),
    Conta(9, "Pessoal e Encargos", "DESPESAS"),
    Conta(10, "Uso de Bens e Serviços", "DESPESAS"),
    Conta(11, "Financeiras", "DESPESAS"),
    Conta(12, "Exploração de Bens e Serviços", "RECEITAS"),
    Conta(13, "Financeiras", "RECEITAS")
]

# Inicializando a gestão contábil
gestao_contabil = GestaoContabil()

for conta in contas:
    gestao_contabil.adicionar_conta(conta)

# Inicializando a gestão de produtos com integração contábil
gestao_produtos = GestaoProdutos(gestao_contabil)

# Testando a aplicação
gestao_produtos.listar_produtos()

gestao_produtos.cadastrar_produto(1, "Camiseta", 29.90)
gestao_produtos.cadastrar_produto(2, "Calça Jeans", 99.90)
gestao_produtos.cadastrar_produto(3, "Tênis", 199.90)

gestao_produtos.listar_produtos()

gestao_produtos.buscar_produto(2)
gestao_produtos.buscar_produto(4)

gestao_produtos.remover_produto(2)
gestao_produtos.listar_produtos()

# Gerando o DRE e o Balanço Patrimonial
print("------------------------DRE---------------------------")
gestao_contabil.gerar_dre()
print("------------------------------------------------------\n")

print("----------------------BALANÇO PAT-----------------------")
gestao_contabil.gerar_balanco_patrimonial()
print("------------------------------------------------------\n")

