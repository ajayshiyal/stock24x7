import yfinance as yf

def get_live_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    return data