# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OrdersPage.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QFrame, QLabel, QPushButton,
                               QScrollArea, QSizePolicy, QVBoxLayout, QWidget)


class Ui_OrdersPage(object):
    def setupUi(self, OrdersPage):
        if not OrdersPage.objectName():
            OrdersPage.setObjectName(u"OrdersPage")
        OrdersPage.resize(619, 447)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OrdersPage.sizePolicy().hasHeightForWidth())
        OrdersPage.setSizePolicy(sizePolicy)
        OrdersPage.setStyleSheet(u"background-color: #fff;")
        self.verticalLayout = QVBoxLayout(OrdersPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalFrame = QFrame(OrdersPage)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Title = QLabel(self.verticalFrame)
        self.Title.setObjectName(u"Title")
        self.Title.setStyleSheet(u"color: black; font-size: 20px")

        self.verticalLayout_2.addWidget(self.Title)

        self.scrollArea = QScrollArea(self.verticalFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 581, 345))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.BackButton = QPushButton(self.verticalFrame)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setStyleSheet(u"QPushButton{\n"
                                      "	background-color:#67BA80;\n"
                                      "	color:black;\n"
                                      "}")

        self.verticalLayout_2.addWidget(self.BackButton)

        self.verticalLayout.addWidget(self.verticalFrame)

        self.retranslateUi(OrdersPage)

        QMetaObject.connectSlotsByName(OrdersPage)

    # setupUi

    def retranslateUi(self, OrdersPage):
        OrdersPage.setWindowTitle(QCoreApplication.translate("OrdersPage", u"Form", None))
        self.Title.setText(
            QCoreApplication.translate("OrdersPage", u"<html><head/><body><p align=\"center\">Title</p></body></html>",
                                       None))
        self.BackButton.setText(QCoreApplication.translate("OrdersPage", u"PushButton", None))
    # retranslateUi
