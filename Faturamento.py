import json

with open('dados.json') as f:
    faturamento = json.load(f)

valores_dia = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

menor_valor = min(valores_dia)

maior_valor = max(valores_dia)

valores_dia_util = [valor for valor in valores_dia if valor > 0]

media = sum(valores_dia_util) / len(valores_dia_util)

dias_acima = sum(1 for valor in valores_dia if valor > media)

print('Menor valor de faturamento diário: ',menor_valor)
print('Maior valor de faturamento diário: ',maior_valor)
print('Número de dias com faturamento acima da média mensal: ',dias_acima)