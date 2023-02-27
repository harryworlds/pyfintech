import yfinance as yf
import numpy as np
import pyttsx3
import pandas as pd
import matplotlib.pyplot as plt


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


# def stock_volatility(stock_ticker, days):
#     stock_data = yf.Ticker(stock_ticker).history(period=f"{days}d")
#     daily_returns = stock_data["Close"].pct_change().dropna()
#     standard_deviation = np.std(daily_returns)

#     if standard_deviation < 0.05:
#         result = f"The standard deviation of {stock_ticker}'s daily returns is {standard_deviation:.4f}. This stock can be considered relatively safe to trade."
#     elif standard_deviation >= 0.05 and standard_deviation < 0.1:
#         result = f"The standard deviation of {stock_ticker}'s daily returns is {standard_deviation:.4f}. This stock is moderately safe to trade."
#     else:
#         result = f"The standard deviation of {stock_ticker}'s daily returns is {standard_deviation:.4f}. This stock is considered risky to trade."

#     # Plot the daily returns
#     plt.plot(daily_returns, label=f"{stock_ticker} Daily Returns")
#     # Plot the standard deviation
#     plt.axhline(standard_deviation, color='red',
#                 label=f"Standard Deviation ({standard_deviation:.4f})")
#     # Add title, labels, and legend
#     plt.title(f"{stock_ticker} Daily Returns and Standard Deviation")
#     plt.xlabel("Time")
#     plt.ylabel("Returns")
#     plt.legend()
#     # Show the plot
#     plt.show()

#     print(result)
#     tts = pyttsx3.init()
#     tts.setProperty('rate', 160)
#     tts.say(result)
#     tts.runAndWait()


# def volatility_test(stock_list, days):

    # for stock in stock_list:
    #     print(f"\nStock: {stock}")
    #     stock_volatility(stock, days)


# stock_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']
# volatility_test(stock_list, "1y")


def stock_volatility(close_prices):
    '''The number of days to consider for a volatility test in stock market depends on various factors such as the type of security, 
    the time frame of the analysis, and the level of detail you want to achieve. 
    However, a common practice is to consider at least 60 to 252 trading days (i.e., roughly 3 to 12 months) to capture the short-term and long-term volatility patterns.
    This time frame allows for a good representation of the market's ups and downs and provides a reliable measure of the stock's historical volatility.

    It's important to note that the stock market is inherently volatile and it's common to see fluctuations in prices on a daily basis. 
    By using a longer time frame, you can get a better understanding of the underlying trends and patterns in the stock's price movements. 
    However, it's also important to keep in mind that past performance is not indicative of future results,
    and the stock's volatility can change over time due to various factors such as economic conditions, company-specific events, and market sentiment.'''

    '''Day trading, it's common to consider a shorter time frame when measuring standard deviation, such as the last 20 to 50 trading days. 
    This time frame provides a good representation of the stock's short-term volatility, 
    which is important in day trading where the goal is to take advantage of price movements over a single day or a few days.

    However, it's important to keep in mind that the stock market is inherently volatile and it's common to see fluctuations in prices on a daily basis. 
    By using a shorter time frame, you may miss important trends and patterns in the stock's price movements. 
    It's a good idea to consider a longer time frame as well to get a better understanding of the stock's overall volatility.

    Ultimately, the number of days to consider for measuring standard deviation depends on your trading strategy, the type of security, 
    and the level of detail you want to achieve. It's a good idea to experiment with different time frames and see which one works best for your particular situation.'''
    '''For long-term holders, it's common to consider a longer time frame when measuring standard deviation, such as the last 5 to 10 years. 
    
    This time frame provides a good representation of the stock's long-term volatility and allows for a more comprehensive analysis of the stock's price movements over a longer period of time.

    A lower standard deviation indicates that the stock has been less volatile over the long-term, while a higher standard deviation indicates greater volatility. 
    Long-term holders typically look for stocks with lower volatility as they are less likely to experience large price swings over a longer period of time.

    However, it's important to keep in mind that the stock market is inherently volatile and it's common to see fluctuations in prices over a long period of time. 
    By using a longer time frame, you may miss important short-term trends and patterns in the stock's price movements. 
    It's a good idea to consider a shorter time frame as well to get a better understanding of the stock's overall volatility.

    Ultimately, the number of days to consider for measuring standard deviation depends on your investment strategy, the type of security, and the level of detail you want to achieve. 
    It's a good idea to experiment with different time frames and see which one works best for your particular situation.'''

    daily_returns = close_prices.pct_change().dropna()
    standard_deviation = np.std(daily_returns)

    if standard_deviation < 0.05:
        result = f"The standard deviation of the stock's daily returns is {standard_deviation:.4f}. This stock can be considered relatively safe to trade."
    elif standard_deviation >= 0.05 and standard_deviation < 0.1:
        result = f"The standard deviation of the stock's daily returns is {standard_deviation:.4f}. This stock is moderately safe to trade."
    else:
        result = f"The standard deviation of the stock's daily returns is {standard_deviation:.4f}. This stock is considered risky to trade."

    # Plot the daily returns
    plt.figure(figsize=(15, 6))
    plt.plot(daily_returns, label="Stock Daily Returns")
    # Plot the standard deviation
    plt.axhline(standard_deviation, color='red',
                label=f"Standard Deviation ({standard_deviation:.4f})")
    # Add title, labels, and legend
    plt.title("Stock Daily Returns and Standard Deviation")
    plt.xlabel("Time")
    plt.ylabel("Returns")
    plt.legend()
    # Show the plot
    plt.show()

    print(result)
    tts = pyttsx3.init()
    tts.setProperty('rate', 160)
    tts.say(result)
    tts.runAndWait()
