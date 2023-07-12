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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QTabWidget,
    QWidget)

class Ui_docViewerWindow(object):
    def setupUi(self, docViewerWindow):
        if not docViewerWindow.objectName():
            docViewerWindow.setObjectName(u"docViewerWindow")
        docViewerWindow.setWindowModality(Qt.NonModal)
        docViewerWindow.resize(333, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(docViewerWindow.sizePolicy().hasHeightForWidth())
        docViewerWindow.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(docViewerWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(docViewerWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        sizePolicy1.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy1)
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(docViewerWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(docViewerWindow)
    # setupUi

    def retranslateUi(self, docViewerWindow):
        docViewerWindow.setWindowTitle(QCoreApplication.translate("docViewerWindow", u"docViewerWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("docViewerWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("docViewerWindow", u"Tab 2", None))
    # retranslateUi

