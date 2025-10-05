import joblib
import tensorflow as tf
import numpy as np
import os
from sklearn.preprocessing import StandardScaler

tickers = ["AAPL", "AMZN", "BA", "BAC", "CAT", "CVX", "GE", "GOOG", "GS", "INTC", "JNJ", "JPM", "KO", "MA", "META", "MRNA", "MSFT", "NKE", "NVDA", "PEP", "PFE", "SBUX", "TSLA", "V", "WMT", "XON"]

model_filename = "StockTraderNetwork2.keras"
scaler_filename = os.path.join("DataTraining", "scaler.pkl")
stock_network = tf.keras.models.load_model(model_filename)

pred_filepath = os.path.join("DataTraining", "x_pred.npy")
x_pred = np.load(pred_filepath)
scaler = joblib.load(scaler_filename)
x_pred = scaler.fit_transform(x_pred)

predictions = stock_network.predict(x_pred)

for ticker, p in zip(tickers, predictions.flatten()):
    if p < .5:
        print(f"{ticker}: {(1-p)*100:.2f}% chance to drop")
    else:
        print(f"{ticker}: {p*100:.2f}% chance to jump")

