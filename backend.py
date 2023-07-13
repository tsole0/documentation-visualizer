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
        profile = CustomWebEngineProfile(self)
        self.webEngineViewer.setPage(QtWebEngineWidgets.QWebEnginePage(profile, self.webEngineViewer))
        self.webEngineViewer.load(url)


class CustomWebEngineProfile(QtWebEngineCore.QWebEngineProfile):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.requestStarted.connect(self.interceptRequest)

    def interceptRequest(self, request):
        url = request.url().toString()
        if url.startswith("http://") or url.startswith("https://"):
            # Allow loading external resources
            request.setHeader(b"Access-Control-Allow-Origin", b"*")
        else:
            # Allow loading local file resources
            request.setHeader(b"Access-Control-Allow-Origin", b"null")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()
