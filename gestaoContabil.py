from lancamentoContabil import LancamentoContabil
class GestaoContabil:
    def __init__(self):
        self.contas = {}
        self.lancamentos = []

    def adicionar_conta(self, conta):
        self.contas[conta.numero] = conta

    def realizar_lancamento(self, data, numero_conta, valor):
        if numero_conta in self.contas:
            conta = self.contas[numero_conta]
            lancamento = LancamentoContabil(data, conta, valor)
            self.lancamentos.append(lancamento)

            conta.creditar(valor)

            if conta.natureza == "ATIVO":
                self.contas[8].debitar(valor)  # Débito na conta "Resultados"
            elif conta.natureza == "DESPESAS":
                self.contas[8].debitar(valor)  # Débito na conta "Resultados"
            elif conta.natureza == "PASSIVO":
                self.contas[8].creditar(valor)  # Crédito na conta "Resultados"
            elif conta.natureza == "RECEITAS":
                self.contas[8].debitar(valor)  # Débito na conta "Resultados"

            print("Lançamento contábil realizado com sucesso!")
        else:
            print("Conta contábil não encontrada.")
            
    def gerar_dre(self):
        receitas = []
        despesas = []

        for lancamento in self.lancamentos:
            conta = lancamento.conta
            if conta.natureza == "DESPESAS":
                despesas.append(lancamento)
            elif conta.natureza == "RECEITAS":
                receitas.append(lancamento)

        print("Demonstrativo de Resultado de Exercício (DRE):")
        print("Receitas:")
        for receita in receitas:
            print(f"{receita.conta.nome}: R${receita.valor:.2f}")
        print("Despesas:")
        for despesa in despesas:
            print(f"{despesa.conta.nome}: R${despesa.valor:.2f}")

        resultado = sum(receita.valor for receita in receitas) - sum(despesa.valor for despesa in despesas)
        print(f"Resumo de Lucros ou Prejuízos: R${resultado:.2f}")

    def gerar_balanco_patrimonial(self):
        balanco = {
            "Ativo": {},
            "Passivo": {}
        }

        for numero, conta in self.contas.items():
            if conta.natureza == "ATIVO":
                balanco["Ativo"][conta.nome] = conta.saldo
            elif conta.natureza == "PASSIVO":
                balanco["Passivo"][conta.nome] = conta.saldo

        print("Balanço Patrimonial:")
        print("Ativo:")
        for conta, saldo in balanco["Ativo"].items():
            print(f"{conta}: R${saldo:.2f}")

        print("Passivo:")
        for conta, saldo in balanco["Passivo"].items():
            print(f"{conta}: R${saldo:.2f}")
