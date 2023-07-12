import sys
from os.path import abspath
from PySide6 import QtGui, QtWebEngineWidgets, QtCore, QtWidgets

from ui_docViewer import Ui_docViewerWindow


# Load the HTML file


class Window(Ui_docViewerWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_docViewerWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Documentation Viewer")
        # self.load_html()

    def load_html(self):
        html = abspath("../sasview/docs/sphinx-docs/build/html/index.html")
        self.ui.webEngineViewer.setUrl(QtCore.QUrl.fromLocalFile(html))
        # Show the web view in a window


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = Window()
    win.show()
    app.exec()