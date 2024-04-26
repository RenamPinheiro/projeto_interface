import requests
from tkinter import *

import yfinance as yf

tempo = str  

def analise_investimento():

    ticker = inserir_ticker.get()

    dados = yf.Ticker(ticker).history(tempo)
    fechamento = dados.Close

    maximo_fechamento = round(fechamento.max(), 2)
    minimo_fechamento = round(fechamento.min(), 2)
    atual_fechamento = round(fechamento[-1])

    texto = f'''
    Cotação Máxima: R$ {maximo_fechamento}
    Cotação Mínima: R$ {minimo_fechamento}
    Cotação Atual: R$ {atual_fechamento}
    '''

    texto_cotacoes['text'] = texto  

def definir_tempo(periodo):
    global tempo
    tempo = periodo

janela = Tk()

janela.title('Análise de Investimento')

janela.geometry('250x300')

grupo_ticker = Frame(janela)
grupo_ticker.grid(row=0, column=0, padx=10, pady=10)

grupo_periodo = Frame(janela)
grupo_periodo.grid(row=1, column=0, padx=10, pady=10)

grupo_botoes = Frame(janela)
grupo_botoes.grid(row=2, column=0, padx=10, pady=10)

texto_ticker = Label(grupo_ticker, text='Ticker')
texto_ticker.grid(column=0, row=0, padx=10, pady=10)

inserir_ticker = Entry(grupo_ticker)
inserir_ticker.grid(column=1, row=0, padx=10, pady=10)

texto_periodo = Label(grupo_periodo, text='Período')
texto_periodo.grid(column=0, row=1, padx=10, pady=10)

botao_periodo1 = Button(grupo_periodo, text='1d', command=lambda: definir_tempo('1d'))
botao_periodo1.grid(column=1, row=1, padx=10, pady=10)

botao_periodo2 = Button(grupo_periodo, text='5d', command=lambda: definir_tempo('5d'))
botao_periodo2.grid(column=2, row=1, padx=10, pady=10)

botao_periodo3 = Button(grupo_periodo, text='3m', command=lambda: definir_tempo('3mo'))
botao_periodo3.grid(column=3, row=1, padx=10, pady=10)

botao_periodo4 = Button(grupo_periodo, text='6m', command=lambda: definir_tempo('6mo'))
botao_periodo4.grid(column=1, row=2, padx=10, pady=10)

botao_periodo5 = Button(grupo_periodo, text='1a', command=lambda: definir_tempo('1y'))
botao_periodo5.grid(column=2, row=2, padx=10, pady=10)

botao_periodo6 = Button(grupo_periodo, text='5a', command=lambda: definir_tempo('5y'))
botao_periodo6.grid(column=3, row=2, padx=10, pady=10)

botao_confirmar = Button(janela, text='Confirmar', command=analise_investimento)
botao_confirmar.grid(column=0, row=2, padx=10, pady=10)

texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=3, padx=10, pady=10)

janela.mainloop()