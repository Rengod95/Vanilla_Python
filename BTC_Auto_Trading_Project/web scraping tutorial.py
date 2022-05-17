import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pybithumb
import time

tickers = ["BTC", "ETH", "BCH", "ETC"]
form_class = uic.loadUiType("btc.ui")[0]

class worker(QThread):
    finished = pyqtSignal(dict)

    def run(self):
        while True:
            data = {}

            for ticker in tickers:
                data[ticker] = self.infos(ticker)

            self.finished.emit(data)
            time.sleep(2)

    def infos(self, ticker):
        try:
            df = pybithumb.get_ohlcv(ticker)
            ma5 = df['close'].rolling(window=5).mean()
            last_ma5 = ma5[-2]
            price = pybithumb.get_current_price(ticker)
            state = None
            if price>last_ma5:
                state = '상승장'
            else:
                state = '하락장'

            return price, last_ma5, state
        except:
            return None, None, None

class Mywindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.worker = worker()
        self.worker.finished.connect(self.update_table_widget)
        self.worker.start()

    @pyqtSlot(dict)
    def update_table_widget(self, data):
        try:
            for ticker, info in data.items():
                index = tickers.index(ticker)

                self.tablewidget.setItem(index, 0, QTableWidgetItem(ticker))
                self.tablewidget.setItem(index, 1, QTableWidgetItem(str(info[0])))
                self.tablewidget.setItem(index, 2, QTableWidgetItem(str(info[1])))
                self.tablewidget.setItem(index, 3, QTableWidgetItem(str(info[2])))
        except:
            pass

app = QApplication(sys.argv)
win = Mywindow()
win.show()
app.exec()
