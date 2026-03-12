import statistics as s

#entrada
lote1 = int(input('Produção lote 1: '))
lote2 = int(input('Produção lote 2: '))
lote3 = int(input('Produção lote 3: '))

#processamento
media = s.mean( (lote1,lote2,lote3) )
desvio = s.stdev( (lote1,lote2,lote3) )

#saída
print(f'Média entre os lotes: {media:.2f}')
print(f'Desvio padrão: {desvio:.2f}')