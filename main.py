from download_yahoo import DownloadYahoo
from optmiser import Optimisier

if __name__ == "__main__":
    title = ["AAL", "DAL", "UAL", "LUV", "HA"]
    start_date = "2023-01-01"
    end_date = "2023-02-01"
    data = DownloadYahoo(title, start_date, end_date).get_data()
    transactions = Optimisier().get_transactions(data)
    print(transactions)
    amount = 1000000
    stock = 0
    for transaction in transactions:
        # print(transaction)
        if transaction.action == "BUY":
            stock = amount / transaction.day.open
            amount = 0
        else:
            amount += transaction.day.open * stock
            stock = 0
        print(amount)
    print(data[0].days[0].date)