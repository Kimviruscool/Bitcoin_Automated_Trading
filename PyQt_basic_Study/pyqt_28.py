# 상승장 하락장 테스트

import pybithumb
from pyqt_27 import bull_market

tickers = pybithumb.get_tickers()
for ticker in tickers:
    is_bull = bull_market(ticker)
