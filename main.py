from download_yahoo import DownloadYahoo
from optmiser import Optimisier

if "__name__" == "__main__":
    title = []
    start_date = "2023-01-01"
    end_date = "2023-02-01"
    data = DownloadYahoo(title, start_date, end_date).get_data()
    transactions = Optimisier().get_transactions(data)