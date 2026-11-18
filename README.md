# RentSmart - R.M Imóveis

Aplicação em Python (Programação Orientada a Objetos) que calcula o orçamento de locação de casas, apartamentos e estúdios da R.M Imóveis, mostra um resumo detalhado e gera um arquivo CSV com a projeção dos 12 primeiros meses de contrato.

## Requisitos

- Python 3.8 ou superior
- Nenhuma biblioteca externa (usa apenas o módulo `csv` da biblioteca padrão)

## Como executar

1. Baixe ou clone o repositório:
   ```bash
   git clone <link-do-repositorio>
   cd <pasta-do-repositorio>
   ```
2. Execute o programa:
   ```bash
   python rentsmart.py
   ```
   (em alguns sistemas, use `python3 rentsmart.py`)
3. Responda às perguntas no terminal.
4. Ao final, o arquivo `projecao_12_meses.csv` será criado na mesma pasta.

## Regras de negócio implementadas

| Item | Regra |
|---|---|
| Aluguel-base | Apartamento 1 quarto: R$ 700 / Casa 1 quarto: R$ 900 / Estúdio: R$ 1.200 |
| Segundo quarto | Apartamento: + R$ 200 / Casa: + R$ 250 |
| Garagem (casa e apto) | 1 vaga: + R$ 300 |
| Garagem (estúdio) | Pacote de 2 vagas: R$ 250 + R$ 60 por vaga adicional |
| Desconto | Apartamento sem crianças: 5% sobre o aluguel já com os adicionais |
| Taxa contratual | R$ 2.000, parcelável em 1 a 5 vezes (cobrada separadamente do aluguel) |

### Premissas adotadas

- No estúdio, quem deseja 1 ou 2 vagas paga o pacote de R$ 250; com 0 vagas não há custo de estacionamento.
- Casas e apartamentos aceitam 0 ou 1 vaga de garagem.
- A pergunta sobre crianças só é feita para apartamentos.
- A taxa contratual é dividida em parcelas iguais, cobradas nos primeiros meses do contrato.

## Exemplo de uso

```
=== RentSmart - R.M Imóveis ===
1 - Apartamento
2 - Casa
3 - Estúdio
Escolha o tipo de imóvel: 1
Quantos quartos (1 ou 2)? 2
Deseja vaga de garagem? (s/n): s
Possui crianças? (s/n): n
Parcelar a taxa em quantas vezes (1 a 5)? 3

===== RESUMO DO ORÇAMENTO =====
Imóvel: Apartamento (2 quarto(s))
Aluguel-base: R$ 700.00
+ Adicional 2 quartos: R$ 200.00
+ Vaga de garagem: R$ 300.00
Subtotal: R$ 1200.00
- Desconto de 5%: R$ 60.00
ALUGUEL MENSAL: R$ 1140.00

--- Taxa contratual (cobrada à parte) ---
Total: R$ 2000.00
Parcelamento: 3x de R$ 666.67
```

Um exemplo do arquivo gerado está em `exemplo_projecao_12_meses.csv`.

## Arquivo CSV

Colunas: `Mes`, `Aluguel`, `Parcela da Taxa`, `Total do Mes`. O separador é ponto e vírgula (`;`) e os valores usam vírgula decimal, para abrir corretamente no Excel em português.

## Estrutura do código

| Classe | Responsabilidade |
|---|---|
| `Imovel` | Classe base com tipo, aluguel-base, quartos e vagas. Define `calcular_adicionais()` e `calcular_desconto()`. |
| `Apartamento` | Herda de `Imovel`. Adicional de 2 quartos, garagem e desconto de 5% sem crianças. |
| `Casa` | Herda de `Imovel`. Adicional de 2 quartos e garagem. |
| `Estudio` | Herda de `Imovel`. Regra própria de pacote de vagas. |
| `Orcamento` | Recebe um imóvel, calcula subtotal, desconto, aluguel final e parcelas da taxa; exibe o resumo e gera o CSV. |

Funções auxiliares: `ler_numero()` e `ler_sim_nao()` (validação de entradas) e `main()` (fluxo principal).

## Autor

Nome: Luis Felipe Silva Santos
RA: 241744
Turma: ADS.2NB
