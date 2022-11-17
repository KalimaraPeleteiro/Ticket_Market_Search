from pandas_datareader import data as web
import matplotlib.pyplot as plt
from datetime import date
from tkinter import Tk, Label, Button, Entry


# Adquire os dados da entry e envia para a próxima função
def data_collection():
    date = f'{month_entry.get()}-{day_entry.get()}-{year_entry.get()}'
    company = company_entry.get()

    search_ticket(date, company)


# Busca pela ação
def search_ticket(start_date, company):
    today = date.today().strftime("%m-%d-%Y")  # Adquire data atual

    # Busca pela ação
    data_frame = web.DataReader(f'{company}.SA', data_source='yahoo',
                                start=start_date, end=today)
    data_frame["Adj Close"].plot(figsize=(15, 10))
    plt.show()


# Window e suas configurações
window = Tk()
window.resizable(False, False)
window.title('Buscador de Ações')

# Widgets
Label(window, text='Qual a data de início da busca?', padx=10, pady=30,
      font=('Times New Roman', 20)).grid(row=0, column=0, columnspan=3)

Label(window, text='Dia', font=('Times New Roman', 14)).grid(row=1, column=0)
Label(window, text='Mês', font=('Times New Roman', 14)).grid(row=1, column=1)
Label(window, text='Ano', font=('Times New Roman', 14)).grid(row=1, column=2)

day_entry = Entry(window, font=('Times New Roman', 14),
                  justify='center')
day_entry.grid(row=2, column=0, padx=10, pady=10)
month_entry = Entry(window, font=('Times New Roman', 14),
                    justify='center')
month_entry.grid(row=2, column=1, padx=10, pady=10)
year_entry = Entry(window, font=('Times New Roman', 14),
                   justify='center')
year_entry.grid(row=2, column=2, padx=10, pady=10)

Label(window, text='Qual a Empresa que será buscada?', padx=10, pady=30,
      font=('Times New Roman', 20)).grid(row=3, column=0, columnspan=3)
company_entry = Entry(window, font=('Times New Roman', 14),
                      justify='center')
company_entry.grid(row=4, column=0, columnspan=3)

Button(window, text='BUSCAR', font=('Times New Roman', 15),
       command=data_collection).grid(row=5, column=0, columnspan=3,
                                     padx=10, pady=10)

window.mainloop()
