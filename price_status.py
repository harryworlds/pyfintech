# import yfinance as yf
# import numpy as np
# import pyttsx3
# import pandas as pd

# class TextToSpeech:
#     def __init__(self, text, rate=140, volume=1.0):
#         self.text = text
#         self.rate = rate
#         self.volume = volume
#         self.engine = pyttsx3.init()

#     def speak(self):
#         self.engine.setProperty('rate', self.rate)
#         self.engine.setProperty('volume', self.volume)
#         self.engine.say(self.text)
#         self.engine.runAndWait()
#         self.engine.stop()

#     def save_to_file(self, file_name):
#         self.engine.save_to_file(self.text, file_name)
#         self.engine.runAndWait()

# def analyze_stocks(stock_list):
#     # Mine data from the Yahoo Finance API and store it as a list of dataframes
#     stock_insight = [yf.Ticker(i).history(period="365d") for i in stock_list]

#     # Define a function to perform 7-day analysis on a stock dataframe
#     def seven_days(df):
#         open_minimum = df.tail(7).describe()[3:4]['Open'][0]
#         close_minimum = df.tail(7).describe()[3:4]['Close'][0]
#         open_maximum = df.tail(7).describe()[7:8]['Open'][0]
#         close_maximum = df.tail(7).describe()[7:8]['Close'][0]
#         open_mean = df.tail(7)["Open"].mean()
#         close_mean = df.tail(7)["Close"].mean()
#         open_variance = np.var(df.tail(7)["Open"])
#         close_variance = np.var(df.tail(7)["Close"])
#         open_stddev = np.std(df.tail(7)["Open"])
#         close_stddev = np.std(df.tail(7)["Close"])
#         return (open_minimum, close_minimum, open_maximum, close_maximum, open_mean, close_mean, open_variance, close_variance, open_stddev, close_stddev)

#     # Use the map function to apply the seven_days function to all stock dataframes in the stock_insight list
#     seven_day_analysis = list(map(seven_days, stock_insight))

#     # Use the zip function to combine the results with the stock list and create a list of tuples
#     result = list(zip(stock_list, seven_day_analysis))

#     for stock, analysis in result:
#         open_min, close_min, open_max, close_max, open_mean, close_mean, open_variance, close_variance, open_stddev, close_stddev = analysis
#         print(f"Stock: {stock}")
#         print(f"7-day Open mean:\t\t{round(open_mean,2)}")
#         print(f"7-day Close mean:\t\t{round(close_mean,2)}")
#         print(f"7-day Open variance:\t{round(open_variance,2)}")
#         print(f"7-day Close variance:\t{round(close_variance,2)}")
#         print(f"7-day Open standard deviation:\t{round(open_stddev,2)}")
#         print(f"7-day Close standard deviation:\t{round(close_stddev,2)}")
#         print(f"7-day Open maximum:\t\t{round(open_max,2)}")
#         print(f"7-day Open minimum:\t\t{round(open_min,2)}")
#         print(f"7-day Close maximum:\t\t{round(close_max,2)}")
#         print(f"7-day Close minimum:\t\t{round(close_min,2)}")
#         print()
#         tts = TextToSpeech(f'{stock} has a mean Open price of {round(open_mean,2)} dollars in the last 7 days, with a minimum Open price of {round(open_min,2)} dollars, a maximum Open price of {round(open_max,2)} dollars, and a standard deviation of {round(open_stddev,2)} dollars')
#         tts.speak()
#         tts.save_to_file(f"{stock}.mp3")

import yfinance as yf
import numpy as np
import pyttsx3
import pandas as pd


class TextToSpeech:
    def __init__(self, text, rate=140, volume=1.0):
        self.text = text
        self.rate = rate
        self.volume = volume
        self.engine = pyttsx3.init()

    def speak(self):
        self.engine.setProperty('rate', self.rate)
        self.engine.setProperty('volume', self.volume)
        self.engine.say(self.text)
        self.engine.runAndWait()
        self.engine.stop()

    def save_to_file(self, file_name):
        self.engine.save_to_file(self.text, file_name)
        self.engine.runAndWait()


class StockAnalysis:
    def __init__(self, stock_list):
        self.stock_list = stock_list
        self.stock_insight = [yf.Ticker(i).history(
            period="365d") for i in self.stock_list]

    def analyze(self):
        # Define a function to perform 7-day analysis on a stock dataframe
        def seven_days(df):
            open_minimum = df.tail(7).describe()[3:4]['Open'][0]
            close_minimum = df.tail(7).describe()[3:4]['Close'][0]
            open_maximum = df.tail(7).describe()[7:8]['Open'][0]
            close_maximum = df.tail(7).describe()[7:8]['Close'][0]
            open_mean = df.tail(7)["Open"].mean()
            close_mean = df.tail(7)["Close"].mean()
            open_variance = np.var(df.tail(7)["Open"])
            close_variance = np.var(df.tail(7)["Close"])
            open_stddev = np.std(df.tail(7)["Open"])
            close_stddev = np.std(df.tail(7)["Close"])
            return (open_minimum, close_minimum, open_maximum, close_maximum, open_mean, close_mean, open_variance, close_variance, open_stddev, close_stddev)

        # Use the map function to apply the seven_days function to all stock dataframes in the stock_insight list
        seven_day_analysis = list(map(seven_days, self.stock_insight))

        # Use the zip function to combine the results with the stock list and create a list of tuples
        result = list(zip(self.stock_list, seven_day_analysis))

        for stock, analysis in result:
            open_min, close_min, open_max, close_max, open_mean, close_mean, open_variance, close_variance, open_stddev, close_stddev = analysis
            print(f"Stock: {stock}")
            print(f"7-day Open mean:\t\t{round(open_mean,2)} dollars")
            print(f"7-day Close mean:\t\t{round(close_mean,2)} dollars")
            print(f"7-day Open variance:\t\t{round(open_variance,2)} dollars")
            print(
                f"7-day Close variance:\t\t{round(close_variance,2)} dollars")
            print(
                f"7-day Open standard deviation:\t{round(open_stddev,2)} dollars")
            print(
                f"7-day Close standard deviation:\t{round(close_stddev,2)} dollars")
            print(
                f"7-day Open maximum:\t\t{round(open_max,2)} dollars ({self.stock_insight[0].index[-1].strftime('%Y-%m-%d')})")
            print(
                f"7-day Open minimum:\t\t{round(open_min,2)} dollars ({self.stock_insight[0].index[-7].strftime('%Y-%m-%d')})")
            print(
                f"7-day Close maximum:\t\t{round(close_max,2)} dollars ({self.stock_insight[0].index[-1].strftime('%Y-%m-%d')})")
            print(
                f"7-day Close minimum:\t\t{round(close_min,2)} dollars ({self.stock_insight[0].index[-7].strftime('%Y-%m-%d')})")
            print()
            tts = TextToSpeech(
                f'Stock {stock} has a mean Open price of {round(open_mean,2)} dollars in the last 7 days. The minimum Open price was {round(open_min,2)} dollars on {self.stock_insight[0].index[-7].strftime("%Y-%m-%d")}. The maximum Open price was {round(open_max,2)} dollars on {self.stock_insight[0].index[-1].strftime("%Y-%m-%d")}. The standard deviation of the Open price was {round(open_stddev,2)} dollars.')
            tts.speak()
            tts.save_to_file(f"{stock}.mp3")

# analysis = StockAnalysis(['AAPL', 'GOOG', 'MSFT', 'AMZN'])
# analysis.analyze()
