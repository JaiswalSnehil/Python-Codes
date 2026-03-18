import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("AAPL", period="3mo", progress=False)
dna = data["Close"].pct_change().fillna(0).values

plt.figure(figsize=(10,1.8))
plt.imshow([dna], aspect="auto", cmap="plasma")
plt.yticks([])
plt.xlabel("Time")
plt.title("Market DNA = AAPL")
plt.show()