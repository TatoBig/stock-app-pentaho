from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys


class Main(QMainWindow):

    # constructor
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)

        button = QPushButton(self)
        button.setText("Iniciar Pentaho Server")
        self.setCentralWidget(button)
        button.clicked.connect(self.on_click)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://localhost:8080/"))
        self.browser.loadFinished.connect(self.update_title)

        self.show()

    @pyqtSlot()
    def on_click(self):
        self.setCentralWidget(self.browser)
        self.showMaximized()

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - Stock App Pentaho" % title)





app = QApplication(sys.argv)
app.setApplicationName("Stock App Pentaho")
window = Main()

app.exec_()
