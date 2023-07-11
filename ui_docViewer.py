# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'docViewer.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_docViewerWindow(object):
    def setupUi(self, docViewerWindow):
        if not docViewerWindow.objectName():
            docViewerWindow.setObjectName(u"docViewerWindow")
        docViewerWindow.resize(711, 806)
        self.horizontalLayoutWidget = QWidget(docViewerWindow)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 770, 691, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(35, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editButton = QPushButton(self.horizontalLayoutWidget)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setMinimumSize(QSize(93, 28))

        self.horizontalLayout.addWidget(self.editButton)

        self.cancelButton = QPushButton(self.horizontalLayoutWidget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setMinimumSize(QSize(93, 28))

        self.horizontalLayout.addWidget(self.cancelButton)

        self.webEngineViewer = QWebEngineView(docViewerWindow)
        self.webEngineViewer.setObjectName(u"webEngineViewer")
        self.webEngineViewer.setGeometry(QRect(9, 9, 691, 751))

        self.retranslateUi(docViewerWindow)

        QMetaObject.connectSlotsByName(docViewerWindow)
    # setupUi

    def retranslateUi(self, docViewerWindow):
        docViewerWindow.setWindowTitle(QCoreApplication.translate("docViewerWindow", u"Dialog", None))
        self.editButton.setText(QCoreApplication.translate("docViewerWindow", u"Edit", None))
        self.cancelButton.setText(QCoreApplication.translate("docViewerWindow", u"Cancel", None))
    # retranslateUi

