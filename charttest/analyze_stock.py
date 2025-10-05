import json
import matplotlib.pyplot as plt
from datetime import datetime

# Load your JSON data
with open('AAPL_Historical.json', 'r') as f:
    data = json.load(f)

time_series = data["Time Series (Daily)"]

# Extract dates and closing prices (sorted by date)
dates = sorted(time_series.keys())
closing_prices = [float(time_series[date]["4. close"]) for date in dates]

# Convert date strings to datetime objects for better plotting
dates = [datetime.strptime(date, '%Y-%m-%d') for date in dates]

# Plot
plt.figure(figsize=(10,5))
plt.plot(dates, closing_prices, marker='o')
plt.title('Apple Stock Closing Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.grid(True)
plt.tight_layout()
plt.show()



"""import json

# Load JSON data from file
with open('AAPL_Historical.json', 'r') as f:
    data = json.load(f)

# Access the "Time Series (Daily)" dictionary
time_series = data["Time Series (Daily)"]

# Example: Print all dates and their closing prices
for date, daily_data in sorted(time_series.items()):
    close_price = daily_data["4. close"]
    print(f"Date: {date}, Close Price: {close_price}")

# Example: Calculate the average closing price
closing_prices = [float(daily_data["4. close"]) for daily_data in time_series.values()]
average_close = sum(closing_prices) / len(closing_prices)
print(f"\nAverage Closing Price: {average_close:.2f}")


"""