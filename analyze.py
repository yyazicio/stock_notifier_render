
import yfinance as yf
import pandas as pd

def fetch_and_analyze(tickers):
    data = []
    for t in tickers:
        try:
            stock = yf.Ticker(t)
            info = stock.info
            pe = info.get('trailingPE', None)
            pb = info.get('priceToBook', None)
            peg = info.get('pegRatio', None)
            price = info.get('currentPrice', None)
            name = info.get('shortName', t)

            if pe and pb and peg:
                score = (1/pe + 1/pb + 1/peg) / 3
                data.append([name, t, pe, pb, peg, price, score])
        except Exception:
            pass

    df = pd.DataFrame(data, columns=['Name', 'Ticker', 'P/E', 'P/B', 'PEG', 'Price', 'ValueScore'])
    df.sort_values('ValueScore', ascending=False, inplace=True)
    undervalued = df.head(5)
    overvalued = df.tail(5)
    return undervalued, overvalued
