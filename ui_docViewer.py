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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_docViewerWindow(object):
    def setupUi(self, docViewerWindow):
        if not docViewerWindow.objectName():
            docViewerWindow.setObjectName(u"docViewerWindow")
        docViewerWindow.resize(710, 806)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(docViewerWindow.sizePolicy().hasHeightForWidth())
        docViewerWindow.setSizePolicy(sizePolicy)
        docViewerWindow.setMinimumSize(QSize(10, 10))
        self.gridLayout = QGridLayout(docViewerWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(35, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.editButton = QPushButton(docViewerWindow)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setMinimumSize(QSize(93, 28))

        self.horizontalLayout.addWidget(self.editButton)

        self.cancelButton = QPushButton(docViewerWindow)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setEnabled(True)
        self.cancelButton.setMinimumSize(QSize(93, 28))

        self.horizontalLayout.addWidget(self.cancelButton)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.webEngineViewer = QWebEngineView(docViewerWindow)
        self.webEngineViewer.setObjectName(u"webEngineViewer")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.webEngineViewer.sizePolicy().hasHeightForWidth())
        self.webEngineViewer.setSizePolicy(sizePolicy1)
        self.webEngineViewer.setMinimumSize(QSize(0, 740))

        self.verticalLayout.addWidget(self.webEngineViewer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(docViewerWindow)

        QMetaObject.connectSlotsByName(docViewerWindow)
    # setupUi

    def retranslateUi(self, docViewerWindow):
        docViewerWindow.setWindowTitle(QCoreApplication.translate("docViewerWindow", u"Dialog", None))
        self.editButton.setText(QCoreApplication.translate("docViewerWindow", u"Edit", None))
        self.cancelButton.setText(QCoreApplication.translate("docViewerWindow", u"Cancel", None))
    # retranslateUi

