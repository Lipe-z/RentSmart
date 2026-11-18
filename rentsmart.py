import csv

TAXA_CONTRATO = 2000.00


# ---------------- CLASSES DOS IMÓVEIS ----------------
class Imovel:
    

    def __init__(self, tipo, aluguel_base, quartos, vagas):
        self.tipo = tipo
        self.aluguel_base = aluguel_base
        self.quartos = quartos
        self.vagas = vagas

    def calcular_adicionais(self):
        return []

    def calcular_desconto(self, subtotal, tem_criancas):
        return 0.0


class Apartamento(Imovel):
    def __init__(self, quartos, vagas):
        super().__init__("Apartamento", 700.00, quartos, vagas)

    def calcular_adicionais(self):
        adicionais = []
        if self.quartos == 2:
            adicionais.append(("Adicional 2 quartos", 200.00))
        if self.vagas == 1:
            adicionais.append(("Vaga de garagem", 300.00))
        return adicionais

    def calcular_desconto(self, subtotal, tem_criancas):
        if not tem_criancas:
            return subtotal * 0.05
        return 0.0


class Casa(Imovel):
    def __init__(self, quartos, vagas):
        super().__init__("Casa", 900.00, quartos, vagas)

    def calcular_adicionais(self):
        adicionais = []
        if self.quartos == 2:
            adicionais.append(("Adicional 2 quartos", 250.00))
        if self.vagas == 1:
            adicionais.append(("Vaga de garagem", 300.00))
        return adicionais


class Estudio(Imovel):
    def __init__(self, vagas):
        super().__init__("Estúdio", 1200.00, 1, vagas)

    def calcular_adicionais(self):
        adicionais = []
        if self.vagas > 0:
            adicionais.append(("Pacote de 2 vagas", 250.00))
            if self.vagas > 2:
                extras = self.vagas - 2
                adicionais.append((f"{extras} vaga(s) extra(s) x R$ 60,00", extras * 60.00))
        return adicionais


# ---------------- CLASSE DO ORÇAMENTO ----------------
class Orcamento:
    def __init__(self, imovel, tem_criancas, parcelas):
        self.imovel = imovel
        self.tem_criancas = tem_criancas
        self.parcelas = parcelas
        self.adicionais = imovel.calcular_adicionais()

        self.subtotal = imovel.aluguel_base
        for descricao, valor in self.adicionais:
            self.subtotal += valor

        self.desconto = imovel.calcular_desconto(self.subtotal, tem_criancas)
        self.aluguel_final = self.subtotal - self.desconto
        self.valor_parcela = TAXA_CONTRATO / parcelas

    def mostrar_resumo(self):
        print("\n===== RESUMO DO ORÇAMENTO =====")
        print(f"Imóvel: {self.imovel.tipo} ({self.imovel.quartos} quarto(s))")
        print(f"Aluguel-base: R$ {self.imovel.aluguel_base:.2f}")
        for descricao, valor in self.adicionais:
            print(f"+ {descricao}: R$ {valor:.2f}")
        print(f"Subtotal: R$ {self.subtotal:.2f}")
        if self.desconto > 0:
            print(f"- Desconto de 5%: R$ {self.desconto:.2f}")
        print(f"ALUGUEL MENSAL: R$ {self.aluguel_final:.2f}")
        print("\n--- Taxa contratual (cobrada à parte) ---")
        print(f"Total: R$ {TAXA_CONTRATO:.2f}")
        print(f"Parcelamento: {self.parcelas}x de R$ {self.valor_parcela:.2f}")

    def gerar_csv(self, nome_arquivo="projecao_12_meses.csv"):
        with open(nome_arquivo, "w", newline="", encoding="utf-8-sig") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")
            escritor.writerow(["Mes", "Aluguel", "Parcela da Taxa", "Total do Mes"])
            for mes in range(1, 13):
                if mes <= self.parcelas:
                    parcela = self.valor_parcela
                else:
                    parcela = 0.0
                total = self.aluguel_final + parcela
                escritor.writerow([mes,
                                   f"{self.aluguel_final:.2f}".replace(".", ","),
                                   f"{parcela:.2f}".replace(".", ","),
                                   f"{total:.2f}".replace(".", ",")])
        print(f"\nArquivo '{nome_arquivo}' gerado com sucesso!")


# ---------------- ENTRADA DE DADOS ----------------
def ler_numero(mensagem, minimo, maximo):
    """Pede um número até o usuário digitar algo válido."""
    while True:
        texto = input(mensagem)
        if texto.isdigit() and minimo <= int(texto) <= maximo:
            return int(texto)
        print(f"Valor inválido! Digite um número de {minimo} a {maximo}.")


def ler_sim_nao(mensagem):
    while True:
        resposta = input(mensagem + " (s/n): ").lower()
        if resposta == "s":
            return True
        if resposta == "n":
            return False
        print("Digite apenas 's' ou 'n'.")


def main():
    print("=== RentSmart - R.M Imóveis ===")
    print("1 - Apartamento\n2 - Casa\n3 - Estúdio")
    tipo = ler_numero("Escolha o tipo de imóvel: ", 1, 3)

    tem_criancas = True

    if tipo == 3:
        vagas = ler_numero("Quantas vagas de garagem (0 a 10)? ", 0, 10)
        imovel = Estudio(vagas)
    else:
        quartos = ler_numero("Quantos quartos (1 ou 2)? ", 1, 2)
        vagas = 1 if ler_sim_nao("Deseja vaga de garagem?") else 0
        if tipo == 1:
            tem_criancas = ler_sim_nao("Possui crianças?")
            imovel = Apartamento(quartos, vagas)
        else:
            imovel = Casa(quartos, vagas)

    parcelas = ler_numero("Parcelar a taxa em quantas vezes (1 a 5)? ", 1, 5)

    orcamento = Orcamento(imovel, tem_criancas, parcelas)
    orcamento.mostrar_resumo()
    orcamento.gerar_csv()


if __name__ == "__main__":
    main()
