import sys
from os.path import abspath
from PySide6 import QtGui, QtWebEngineWidgets, QtCore, QtWidgets


# Load the HTML file
app = QtWidgets.QApplication(sys.argv)


class Window(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_html()
        # self.setupUi(self)
        # self.connectSignalsSlots()

    def load_html(self):
        self.view = QtWebEngineWidgets.QWebEngineView()
        html = abspath("../sasview/docs/sphinx-docs/build/html/index.html")
        self.view.setUrl(QtCore.QUrl.fromLocalFile(html))
        # Show the web view in a window
        self.setCentralWidget(self.view)
        self.show()

if __name__ == "__main__":
    win = Window()
    win.show()
    app.exec()