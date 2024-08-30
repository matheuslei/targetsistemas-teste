# Questão 4: Percentual de Faturamento por Estado

def calcular_percentual(faturamento):
    total = sum(faturamento.values())
    percentual = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}
    return percentual

if __name__ == "__main__":
    faturamento = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    percentual = calcular_percentual(faturamento)
    for estado, pct in percentual.items():
        print(f"{estado}: {pct:.2f}%")
