import yfinance as yf

def get_20_year_stock_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="20y")
    return data