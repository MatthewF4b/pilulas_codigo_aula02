import random as r

#entrada
dolar_atual = float(input('Cotação atual do dólar: '))

#processamento
variacao = r.uniform(-0.015, 0.015)
nova_cotacao = dolar_atual * (1 + variacao)

print(f'% de variação simulada: {variacao:.3%}')
print(f'Nova cotação: {nova_cotacao:.4f}')