# Questão 3: Análise de Faturamento Diário

import json

def analyze_faturamento(filename):
    with open(filename, 'r') as file:
        faturamento = json.load(file)

    valores = [dia['valor'] for dia in faturamento if dia['valor'] > 0]
    if not valores:
        print("Nenhum dado de faturamento encontrado.")
        return

    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    dias_acima_media = sum(1 for valor in valores if valor > media)

    print(f"Menor valor de faturamento: R${menor:.2f}")
    print(f"Maior valor de faturamento: R${maior:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

if __name__ == "__main__":
    analyze_faturamento('data/faturamento.json')
