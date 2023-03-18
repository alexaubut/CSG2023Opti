import yfinance as yf

class Day:
    def __init__(self, date:str, open:float):
        self.date = date
        self.open = open

class Title:
    def __init__(self, title:str, days : list[Day]):
        self.title = title
        self.days = days

    def __str__(self) -> str:
        string = f"{self.title}\n"
        for day in self.days:
            string += f"{day.date} {day.open}\n"
        return string
    
    def __repr__(self) -> str:
        return self.__str__()

class DownloadYahoo:
    def __init__(self, titles_str:list[str], start: str, end:str ):
        self.titles = []
        self.titles_str = titles_str
        self.start = start
        self.end = end

        for title in self.titles_str:
            self._download(title, self.start, self.end)

    def _download(self, ticker_symbol:str, start:str, end:str):
        data = yf.download(ticker_symbol, start=start, end=end)
        days = []
        for index, row in data.iterrows():
            days.append(Day(str(index)[0:10], float(row['Open'])))
        self.titles.append(Title(ticker_symbol, days))

    def get_data(self):
        return self.titles

# ticker_symbol = "AAPL"

# # download data for the stock
# data = yf.download(ticker_symbol, start="2023-01-01", end="2023-02-01")

# # display the downloaded data
# print(data)

# data2 = DownloadYahoo(["AAPL"], "2023-01-01", "2023-02-01").get_data()
# print(data2)
