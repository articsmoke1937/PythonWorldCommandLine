import matplotlib.pyplot as plt
import datetime as dt
import University.globals as globals
import yfinance as yf

def stock_plot1(co,stocks,pname):
    for x in range(co):
            s = input(globals.prompt)
            s = s.upper()
            stocks.append(s)
    print(stocks)
    stock_close = yf.download(stocks, period='ytd').Open
    normalized_stock_close = (stock_close/stock_close.iloc[0]*100)
    for x in stocks:
        normalized_stock_close[f'{x}'].plot()
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()
    return(stocks)