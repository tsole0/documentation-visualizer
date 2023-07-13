import sys
from os.path import abspath
from PySide6 import QtGui, QtWebEngineWidgets, QtCore, QtWidgets
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
        profile = QtWebEngineWidgets.QWebEngineProfile.defaultProfile()
        profile.setUrlRequestInterceptor(CustomUrlRequestInterceptor())
        self.webEngineViewer.setPage(QtWebEngineWidgets.QWebEnginePage(profile, self.webEngineViewer))
        self.webEngineViewer.load(url)


class CustomUrlRequestInterceptor(QtWebEngineWidgets.QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, info):
        url = info.requestUrl().toString()
        if url.startswith("http://") or url.startswith("https://"):
            # Allow loading external resources
            info.setHttpHeader(b"Access-Control-Allow-Origin", b"*")
        else:
            # Allow loading local file resources
            info.setHttpHeader(b"Access-Control-Allow-Origin", b"null")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()
