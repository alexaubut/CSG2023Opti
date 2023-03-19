import json
from download_yahoo import Day
class Transaction():
    def __init__(self, date: Day, action, ticker) -> None:
        self.day = date
        self.date = date.date
        self.action = action
        self.ticker = ticker

    def __str__(self) -> str:
        #return json.dumps(self)
        return """{{ 
            "date": "{0}",
            "action": "{1}",
            "ticker": "{2}" 
            }}""".format(self.date, self.action, self.ticker)
    def __repr__(self) -> str:
        return self.__str__()