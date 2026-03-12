import datetime as d
#entrada
data_compra = input('Digite a data da compra d/m/aaaa: ')
garantia = int(input('Prazo de garantia: ')) 

#processamento
data_inicial = d.datetime.strptime(data_compra, '%d/%m/%Y')
data_final = data_inicial + d.timedelta(days=garantia * 30)

#saída
print(f'Término da garantia: {data_final.strftime('%d/%m/%Y')}')
print(f'Dia da semana: {data_final.strftime('%A')}')