import sys
from os.path import abspath
from PySide6 import QtGui, QtWebEngineWidgets, QtCore, QtWidgets, QtWebEngineCore
from ui_docViewer import Ui_docViewerWindow


class Window(QtWidgets.QWidget, Ui_docViewerWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_docViewerWindow()
        self.setupUi(self)
        self.setWindowTitle("Documentation Viewer")
        self.load_html()

    def load_html(self):
        html = abspath("my_docs.html")
        url = QtCore.QUrl.fromLocalFile(html)
        settings = self.webEngineViewer.settings()
        settings.setAttribute(QtWebEngineCore.QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        settings.setAttribute(QtWebEngineCore.QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        self.webEngineViewer.load(url)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()