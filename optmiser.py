from transaction import Transaction
from download_yahoo import Day, Title

class Optimisier():
    def get_transactions(self, data: list[Title]) -> list[Transaction]:
        active_title = None
        transactions = []
        for day in data[0].days[:-4]:
            transaction, new_title = self.get_best_transaction(data, active_title, day)
            if transaction:
                active_title = new_title
                transactions.append(transaction)
        if active_title:
            transactions.append(Transaction(data[0].days[-1], "SELL", active_title.title))
        return transactions

    def get_delta(self, first_day:Day, second_day:Day) -> float:
        return second_day.open / first_day.open
    
    def get_best_transaction(self, data: list[Title], active_title: Title or None, day_obj: Day) -> tuple[Transaction or None, Title or None]:
        day = day_obj.date
        delta_active_title_2_days = None
        delta_active_title_3_days = None
        if active_title:
            delta_active_title_2_days = self.get_delta(active_title.get_date(day), active_title.days[active_title.get_date_by_index(day) + 2] )
            delta_active_title_3_days = self.get_delta(active_title.get_date(day), active_title.days[active_title.get_date_by_index(day) + 3] )
        best_delta = -999999999
        best_title = None
        for title in data:
            delta_3 = self.get_delta(title.days[title.get_date_by_index(day) + 1], title.days[title.get_date_by_index(day) + 3])
            delta_2 = self.get_delta(title.days[title.get_date_by_index(day) + 1], title.days[title.get_date_by_index(day) + 2])
            if delta_2 > best_delta or delta_3 > best_delta:
                if delta_2 > delta_3:
                    best_title = title
                    best_delta = delta_2
                else:
                    best_title = title
                    best_delta = delta_3
        if active_title:
            if ((delta_active_title_2_days < 0 or delta_active_title_2_days < best_delta) and
                (delta_active_title_3_days < 0 or delta_active_title_3_days < best_delta)):
                return (Transaction(day_obj, "SELL", active_title.title), None)
            else:
                return None, None
        if best_delta > 0:
            return (Transaction(day_obj, "BUY", best_title.title), best_title)
        else:
            return None, None