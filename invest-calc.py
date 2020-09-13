
START_AMOUNT = 100000 # Начальная сумма, рублей
ANNUAL_RETURN = 11 # Среднегодовая доходность, в % годовых
ADDITION = 2000 # Сумма ежемесячного пополнения, рублей
PERIOD = 20 # Длительность инвестиций, лет.

months = PERIOD*12
current_assets = START_AMOUNT

for i in range(0, months):		
	profit = current_assets*ANNUAL_RETURN/100/12
	current_assets += ADDITION + profit

print(f'Ежемесячный доход: {round(profit)} руб.')
print(f'Сумма на счету: {round(current_assets)} руб.')

