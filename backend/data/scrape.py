import yfinance as yf

def get_yahoo_finance_data(company_ticker, 
    period = '1d', 
    start = '2010-1-1', 
    end = '2020-4-28'):

    tickerData = yf.Ticker(company_ticker)

    df = tickerData.history(period = 'max')
    df.describe()

    return df


#df = get_yahoo_finance_data('KINV-B.ST')