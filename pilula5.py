import locale as l
l.setlocale(l.LC_ALL,'pt_BR.UTF-8')

#entrada
receita1 = float(input('Valor da receita no mês de abril: '))
receita2 = float(input('Valor da receita no mês de maio: '))
receita3 = float(input('Valor da receita no mês de junho: '))

#processamento
total = receita1+receita2+receita3

#saída
print(f'Abril: {l.currency(receita1, grouping=True)}')
print(f'Maio: {l.currency(receita2, grouping=True)}')
print(f'Junho: {l.currency(receita3, grouping=True)}')
print(f'Total: {l.currency(total, grouping=True)}')
