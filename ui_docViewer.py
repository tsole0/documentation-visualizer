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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_docViewerWindow(object):
    def setupUi(self, docViewerWindow):
        if not docViewerWindow.objectName():
            docViewerWindow.setObjectName(u"docViewerWindow")
        docViewerWindow.setWindowModality(Qt.NonModal)
        docViewerWindow.resize(512, 582)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(docViewerWindow.sizePolicy().hasHeightForWidth())
        docViewerWindow.setSizePolicy(sizePolicy)
        docViewerWindow.setMinimumSize(QSize(30, 30))
        self.gridLayout = QGridLayout(docViewerWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editButton = QPushButton(docViewerWindow)
        self.editButton.setObjectName(u"editButton")

        self.horizontalLayout.addWidget(self.editButton)

        self.cancelButton = QPushButton(docViewerWindow)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.webEngineViewer = QWebEngineView(docViewerWindow)
        self.webEngineViewer.setObjectName(u"webEngineViewer")
        sizePolicy.setHeightForWidth(self.webEngineViewer.sizePolicy().hasHeightForWidth())
        self.webEngineViewer.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.webEngineViewer, 1, 0, 1, 1)


        self.retranslateUi(docViewerWindow)

        QMetaObject.connectSlotsByName(docViewerWindow)
    # setupUi

    def retranslateUi(self, docViewerWindow):
        docViewerWindow.setWindowTitle(QCoreApplication.translate("docViewerWindow", u"docViewerWindow", None))
        self.editButton.setText(QCoreApplication.translate("docViewerWindow", u"Edit", None))
        self.cancelButton.setText(QCoreApplication.translate("docViewerWindow", u"Cancel", None))
    # retranslateUi

