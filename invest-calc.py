import tkinter as tk
import tkinter.font as tkfont

def testVal(inStr,acttyp):
    if acttyp == '1':
        if not inStr.isdigit():
            return False
    return True

def error(error):
	lbl_current_assets.destroy()
	ent_current_assets.destroy()
	lbl_error = tk.Label(text=error, font=bold_font, fg='red')
	lbl_error.grid(column=0, columnspan=2, row=4, pady=3)
	btn_calculate['state'] = 'disabled'
	# return lbl_error

def calculate():

	if ent_start_amount.get() == '':
		current_assets = 0
		ent_start_amount.insert(0, '0')
	else:
		current_assets = int(ent_start_amount.get())

	if ent_annual_return.get() == '':
		annual_return = 0
		ent_annual_return.insert(0, '0')
	else:
		annual_return = int(ent_annual_return.get())

	if ent_addition.get() == '':
		addition = 0
		ent_addition.insert(0, '0')
	else:
		addition = int(ent_addition.get())

	if ent_period.get() == '':
		error('Введите срок инвестиций!')
		frm_period['bg'] = 'red'
		return
	else:
		period = int(ent_period.get())
		if period < 1:
			error('Срок инвестиций должен быть не менее года!')
			frm_period['bg'] = 'red'
			return

	months = period*12
	for i in range(months):
		profit = current_assets*annual_return/100/12
		current_assets += addition + profit
	ent_current_assets['text'] = '{:,}'.format(round(current_assets)).replace(',', ' ')+' руб.'
	ent_current_assets['fg'] = 'black'
	ent_profit['text'] = '{:,}'.format(round(profit)).replace(',', ' ')+' руб.'

def clear():
	frm_clr = tk.Frame()
	frm_clr.grid(column=0, columnspan=2, row=4, padx=5, sticky='nsew')
	global lbl_current_assets
	lbl_current_assets = tk.Label(text='Сумма на счету:')
	global ent_current_assets
	ent_current_assets = tk.Label(width=15, text='')
	lbl_current_assets.grid(column=0, row=4, padx=5, sticky='e')
	ent_current_assets.grid(column=1, row=4, padx=5, pady=3)
	ent_start_amount.delete(0, tk.END)
	ent_annual_return.delete(0, tk.END)
	ent_addition.delete(0, tk.END)
	ent_period.delete(0, tk.END)
	ent_current_assets['text'] = ''
	ent_profit['text'] = ''
	btn_calculate['state'] = 'normal'
	# global frm_period
	frm_period['bg'] = DEFAULT_BORDER_COLOR


window = tk.Tk()
window.title('Инвест-калькулятор')
window.resizable(width=False, height=False)
bold_font = tkfont.Font(family="Helvetica", size=10,weight="bold")

lbl_start_amount = tk.Label(text='Начальная сумма, рублей:')
lbl_start_amount.grid(column=0, row=0, padx=5, sticky='e')

ent_start_amount = tk.Entry(width=15, validate="key")
ent_start_amount['validatecommand'] = (ent_start_amount.register(testVal),'%P','%d')
ent_start_amount.grid(column=1, row=0, padx=5, pady=3)

lbl_annual_return = tk.Label(text='Среднегодовая доходность, в % годовых:')
lbl_annual_return.grid(column=0, row=1, padx=5, sticky='e')

ent_annual_return = tk.Entry(width=15, validate="key")
ent_annual_return['validatecommand'] = (ent_annual_return.register(testVal),'%P','%d')
ent_annual_return.grid(column=1, row=1, padx=5, pady=3)

lbl_addition = tk.Label(text='Сумма ежемесячного пополнения, рублей:')
lbl_addition.grid(column=0, row=2, padx=5, sticky='e')

ent_addition = tk.Entry(width=15, validate="key")
ent_addition['validatecommand'] = (ent_addition.register(testVal),'%P','%d')
ent_addition.grid(column=1, row=2, padx=5, pady=3)

lbl_period = tk.Label(text='Срок инвестиций, лет:')
lbl_period.grid(column=0, row=3, padx=5, sticky='e')

frm_period = tk.Frame(borderwidth=2)
DEFAULT_BORDER_COLOR = frm_period['bg']
frm_period.grid(column=1, row=3, padx=5, pady=1)
ent_period = tk.Entry(frm_period, width=15, validate="key")
ent_period['validatecommand'] = (ent_period.register(testVal),'%P','%d')
ent_period.pack()
# ent_period.grid(column=1, row=3, padx=5, pady=3)

lbl_current_assets = tk.Label(text='Сумма на счету:')
ent_current_assets = tk.Label(width=15, text='')
lbl_current_assets.grid(column=0, row=4, padx=5, sticky='e')
ent_current_assets.grid(column=1, row=4, padx=5, pady=3)

lbl_profit = tk.Label(text='Ежемесячный доход:')
ent_profit = tk.Label(width=15, text='')
lbl_profit.grid(column=0, row=5, padx=5, sticky='e')
ent_profit.grid(column=1, row=5, padx=5, pady=3)

btn_calculate = tk.Button(text='Очистить', width=15, command=clear)
btn_calculate.grid(column=0, row=6, padx=5, pady=4, sticky='e')
btn_calculate = tk.Button(text='Рассчитать', width=15, command=calculate)
btn_calculate.grid(column=1, row=6, padx=5, pady=4)


window.mainloop()