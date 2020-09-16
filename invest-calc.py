import tkinter as tk

def calculate():	
	period = int(ent_period.get())
	months = period*12
	current_assets = int(ent_start_amount.get())
	annual_return = int(ent_annual_return.get())
	addition = int(ent_addition.get())
	for i in range(months):		
		profit = current_assets*annual_return/100/12
		current_assets += addition + profit
	ent_current_assets['text'] = f'{round(current_assets)} руб.'
	ent_profit['text'] = f'{round(profit)} руб.'

def clear():
	ent_start_amount.delete(0, tk.END)
	ent_annual_return.delete(0, tk.END)
	ent_addition.delete(0, tk.END)
	ent_period.delete(0, tk.END)
	ent_current_assets['text'] = ''
	ent_profit['text'] = ''

window = tk.Tk()
window.title('Инвест-калькулятор')

lbl_start_amount = tk.Label(text='Начальная сумма, рублей:')
ent_start_amount = tk.Entry(width=15)
lbl_start_amount.grid(column=0, row=0, padx=5, sticky='e')
ent_start_amount.grid(column=1, row=0, padx=5, pady=3)

lbl_annual_return = tk.Label(text='Среднегодовая доходность, в % годовых:')
ent_annual_return = tk.Entry(width=15)
lbl_annual_return.grid(column=0, row=1, padx=5, sticky='e')
ent_annual_return.grid(column=1, row=1, padx=5, pady=3)

lbl_addition = tk.Label(text='Сумма ежемесячного пополнения, рублей:')
ent_addition = tk.Entry(width=15)
lbl_addition.grid(column=0, row=2, padx=5, sticky='e')
ent_addition.grid(column=1, row=2, padx=5, pady=3)

lbl_period = tk.Label(text='Длительность инвестиций, лет:')
ent_period = tk.Entry(width=15)
lbl_period.grid(column=0, row=3, padx=5, sticky='e')
ent_period.grid(column=1, row=3, padx=5, pady=3)

lbl_current_assets = tk.Label(text='Сумма на счету:')
ent_current_assets = tk.Label(width=15, text='')
lbl_current_assets.grid(column=0, row=4, padx=5, sticky='e')
ent_current_assets.grid(column=1, row=4, padx=5, pady=3)

lbl_profit = tk.Label(text='Ежемесячный доход:')
ent_profit = tk.Label(width=15, text='')
lbl_profit.grid(column=0, row=5, padx=5, sticky='e')
ent_profit.grid(column=1, row=5, padx=5, pady=3)

btn_calculate = tk.Button(text='Очистить', width=15, command=clear)
btn_calculate.grid(column=0, row=6, padx=5, pady=3, sticky='e')
btn_calculate = tk.Button(text='Рассчитать', width=15, command=calculate)
btn_calculate.grid(column=1, row=6, padx=5, pady=3)

window.mainloop()