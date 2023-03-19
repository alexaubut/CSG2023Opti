from transaction import Transaction
from download_yahoo import Day, Title

class Optimisier():
    def get_transactions(self, data: list[Title]) -> list[Transaction]:
        #TODO gérer premier achat
        first_title = None
        transactions = []
        for day in data[0].days[:-2]:
            transaction, new_title = self.get_best_transaction(data, first_title, day)
            if transaction:
                first_title = new_title
                transactions.append(transaction)
        if first_title:
            transactions.append(Transaction(data[0].days[-1], "SELL", first_title.title))
        return transactions
        #TODO gérer 2 derniers jours index error


    def get_delta(self, first_day:Day, second_day:Day) -> float:
        return second_day.open - first_day.open
    
    def get_best_transaction(self, data: list[Title], active_title: Title or None, day_obj: Day) -> tuple[Transaction or None, Title or None]:
        day = day_obj.date
        delta_active_title = None
        if active_title:
            delta_active_title = self.get_delta(active_title.get_date(day), active_title.days[active_title.get_date_by_index(day) + 2] )
        best_delta = -999999999
        best_title = None
        for title in data:
            delta = self.get_delta(title.days[title.get_date_by_index(day) + 1], title.days[title.get_date_by_index(day) + 2])
            if delta > best_delta:
                best_title = title
                best_delta = delta
        if delta_active_title:
            if delta_active_title < 0 or delta_active_title < best_delta:
                return (Transaction(day_obj, "SELL", active_title.title), None)
            else:
                return None, None
        return (Transaction(day_obj, "BUY", best_title.title), best_title)