import json

# Paste your JSON string here or load from a file
json_data = '''{
    "Meta Data": {...},
    "Time Series (Daily)": {
        "2025-10-03": {"1. open": "254.6650", "2. high": "259.2400", "3. low": "253.9500", "4. close": "258.0200", "5. volume": "49155614"},
        "2025-10-02": {...},
        ...
    }
}'''

data = json.loads(json_data)
time_series = data['Time Series (Daily)']

# Extract dates and closing prices
dates = []
closing_prices = []

for date in sorted(time_series.keys()):
    dates.append(date)
    closing_prices.append(float(time_series[date]['4. close']))
