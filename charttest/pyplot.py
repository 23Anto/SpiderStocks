import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(dates, closing_prices, marker='o')
plt.title('AAPL Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
