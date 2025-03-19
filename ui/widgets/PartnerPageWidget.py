# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PartnerPage.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QPixmap)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
                               QPushButton, QScrollArea, QVBoxLayout,
                               QWidget)


class Ui_PartnersPage(object):
    def setupUi(self, PartnersPage):
        if not PartnersPage.objectName():
            PartnersPage.setObjectName(u"PartnersPage")
        PartnersPage.setWindowModality(Qt.WindowModality.NonModal)
        PartnersPage.resize(1090, 644)
        PartnersPage.setStyleSheet(u"background-color:white; color:black;")
        self.verticalLayout_7 = QVBoxLayout(PartnersPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.ss = QFrame(PartnersPage)
        self.ss.setObjectName(u"ss")
        self.ss.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.ss)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.title = QFrame(self.ss)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"padding-left:20px;")
        self.horizontalLayout = QHBoxLayout(self.title)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.title)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 80))
        self.label.setPixmap(QPixmap(u"ui/icons/Master_pol.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.title)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color:black;\n" "font-size:20px;")

        self.horizontalLayout.addWidget(self.label_2)

        self.verticalLayout_4.addWidget(self.title)

        self.scrollArea = QScrollArea(self.ss)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border:1px solid grey")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1050, 396))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scroll = QFrame(self.scrollAreaWidgetContents)
        self.scroll.setObjectName(u"scroll")
        self.scroll.setStyleSheet(u"border:none;")
        self.verticalLayout_2 = QVBoxLayout(self.scroll)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout_3.addWidget(self.scroll)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.button = QFrame(self.ss)
        self.button.setObjectName(u"button")
        self.button.setStyleSheet(u"QPushButton{\n"
                                  "	background-color:#67BA80;\n"
                                  "	color:black;\n"
                                  "}")
        self.verticalLayout_5 = QVBoxLayout(self.button)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton = QPushButton(self.button)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_5.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.button)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_5.addWidget(self.pushButton_2)

        self.verticalLayout_6.addWidget(self.button)

        self.verticalLayout_7.addWidget(self.ss)

        self.retranslateUi(PartnersPage)

        QMetaObject.connectSlotsByName(PartnersPage)

    # setupUi

    def retranslateUi(self, PartnersPage):
        PartnersPage.setWindowTitle(QCoreApplication.translate("PartnersPage", u"parner_page", None))
        self.label.setText("")
        self.label_2.setText(
            QCoreApplication.translate("PartnersPage", u"\u041c\u0430\u0441\u0442\u0435\u0440 \u041f\u043e\u043b",
                                       None))
        self.pushButton.setText(QCoreApplication.translate("PartnersPage", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("PartnersPage", u"PushButton", None))
    # retranslateUi
