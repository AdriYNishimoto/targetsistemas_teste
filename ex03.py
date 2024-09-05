import json

faturamento_json = '''
{
    "faturamento": [1200.45, 2500.12, 0, 3400.56, 0, 3200.32, 4000.00, 1500.80, 0]
}
'''

dados = json.loads(faturamento_json)["faturamento"]

faturamento_valido = [valor for valor in dados if valor > 0]

menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)
media_mensal = sum(faturamento_valido) / len(faturamento_valido)

dias_acima_da_media = len([valor for valor in faturamento_valido if valor > media_mensal])

print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")


# O código carrega um JSON com os valores de faturamento, remove os dias sem faturamento (valores iguais a 0) e calcula o menor valor, o maior valor e quantos dias o faturamento foi superior à média mensal. (numeros simulados)