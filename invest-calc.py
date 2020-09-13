
START_AMOUNT = 12000 # Начальная сумма, рублей
ANNUAL_RETURN = 8 # Среднегодовая доходность, в % годовых
ADDITION = 400 # Сумма ежемесячного пополнения, рублей
PERIOD = 1 # Длительность инвестиций, лет.

months = PERIOD*12
current_assets = START_AMOUNT

for i in range(0, months):		
	profit = current_assets*ANNUAL_RETURN/100/12
	current_assets += ADDITION + profit

print(f'Ежемесячный доход: {round(profit)} руб.')
print(f'Сумма на счету: {round(current_assets)} руб.')

