import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download(["GLD", "SLV"], period="1y")["Close"]

dd_gold = (data["GLD"] / data["GLD"].cummax()-1)*100
dd_silver = (data["SLV"] / data["SLV"].cummax()-1)*100

plt.bar(dd_gold.index, dd_gold, alpha=0.6, label="Gold")
plt.bar(dd_silver.index, dd_silver, alpha=0.6, label="Silver")
plt.title("Drawdown Waterfall (%)")
plt.legend()
plt.show()