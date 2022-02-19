import yfinance as yf

stocklist=['MSFT', 'ASX']

for x in stocklist:
    stock=yf.Ticker(x)
    hist=stock.history()
    print(hist)