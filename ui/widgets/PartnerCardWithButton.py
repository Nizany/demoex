# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PartnerCardWithButton.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_PartnerCardWithButton(object):
    def setupUi(self, PartnerCardWithButton):
        if not PartnerCardWithButton.objectName():
            PartnerCardWithButton.setObjectName(u"PartnerCardWithButton")
        PartnerCardWithButton.resize(900, 180)
        PartnerCardWithButton.setStyleSheet(u"QWidget{\n"
"                background-color: #F4E8D3;\n"
"                color: #000;\n"
"                font-size: 15px; \n"
"                padding: 0px\n"
"                }\n"
"\n"
"            ")
        self.verticalLayout_2 = QVBoxLayout(PartnerCardWithButton)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(PartnerCardWithButton)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u".QFrame{\n"
"                                    border: 2px solid black\n"
"                                    }\n"
"                                ")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PartnerTypeAndName = QPushButton(self.frame)
        self.PartnerTypeAndName.setObjectName(u"PartnerTypeAndName")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PartnerTypeAndName.sizePolicy().hasHeightForWidth())
        self.PartnerTypeAndName.setSizePolicy(sizePolicy)
        self.PartnerTypeAndName.setAutoRepeatInterval(100)

        self.verticalLayout.addWidget(self.PartnerTypeAndName)

        self.BossName = QPushButton(self.frame)
        self.BossName.setObjectName(u"BossName")
        sizePolicy.setHeightForWidth(self.BossName.sizePolicy().hasHeightForWidth())
        self.BossName.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.BossName)

        self.PhoneNumber = QPushButton(self.frame)
        self.PhoneNumber.setObjectName(u"PhoneNumber")
        sizePolicy.setHeightForWidth(self.PhoneNumber.sizePolicy().hasHeightForWidth())
        self.PhoneNumber.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.PhoneNumber)

        self.Rank = QPushButton(self.frame)
        self.Rank.setObjectName(u"Rank")
        sizePolicy.setHeightForWidth(self.Rank.sizePolicy().hasHeightForWidth())
        self.Rank.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.Rank)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.DiscountPercentage = QPushButton(self.frame)
        self.DiscountPercentage.setObjectName(u"DiscountPercentage")
        sizePolicy.setHeightForWidth(self.DiscountPercentage.sizePolicy().hasHeightForWidth())
        self.DiscountPercentage.setSizePolicy(sizePolicy)
        self.DiscountPercentage.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout.addWidget(self.DiscountPercentage, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame)

        self.GetOrdersListButton = QPushButton(PartnerCardWithButton)
        self.GetOrdersListButton.setObjectName(u"GetOrdersListButton")
        sizePolicy.setHeightForWidth(self.GetOrdersListButton.sizePolicy().hasHeightForWidth())
        self.GetOrdersListButton.setSizePolicy(sizePolicy)
        self.GetOrdersListButton.setMaximumSize(QSize(200, 16777215))
        self.GetOrdersListButton.setStyleSheet(u"background-color: #67BA80; border-radius: 10px")

        self.horizontalLayout_2.addWidget(self.GetOrdersListButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(PartnerCardWithButton)

        QMetaObject.connectSlotsByName(PartnerCardWithButton)
    # setupUi

    def retranslateUi(self, PartnerCardWithButton):
        PartnerCardWithButton.setWindowTitle(QCoreApplication.translate("PartnerCardWithButton", u"Form", None))
        self.PartnerTypeAndName.setText(QCoreApplication.translate("PartnerCardWithButton", u"PartnerTypeAndName", None))
        self.BossName.setText(QCoreApplication.translate("PartnerCardWithButton", u"BossName", None))
        self.PhoneNumber.setText(QCoreApplication.translate("PartnerCardWithButton", u"PhoneNumber", None))
        self.Rank.setText(QCoreApplication.translate("PartnerCardWithButton", u"Rank", None))
        self.DiscountPercentage.setText(QCoreApplication.translate("PartnerCardWithButton", u"DiscountPercentage", None))
        self.GetOrdersListButton.setText(QCoreApplication.translate("PartnerCardWithButton", u"PushButton", None))
    # retranslateUi

