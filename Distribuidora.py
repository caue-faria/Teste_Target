faturamento_regiao = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(faturamento_regiao.values())
percentual_regiao = {estado: (faturamento / total) * 100 for estado, faturamento in faturamento_regiao.items()}

for estado, percentual in percentual_regiao.items():
    print(f'{estado}: {percentual:.2f}%')