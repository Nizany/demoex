# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateUpdatePage.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QComboBox)


class Ui_CreateUpdatePage(object):
    def setupUi(self, CreateUpdatePage):
        if not CreateUpdatePage.objectName():
            CreateUpdatePage.setObjectName(u"CreateUpdatePage")
        CreateUpdatePage.resize(500, 362)
        CreateUpdatePage.setMinimumSize(QSize(0, 0))
        CreateUpdatePage.setStyleSheet(u"background-color: #ffffff; color: black;")
        self.verticalLayout_2 = QVBoxLayout(CreateUpdatePage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(CreateUpdatePage)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"color: black; font-size: 15px")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.Type = QLabel(self.frame)
        self.Type.setObjectName(u"Type")

        self.horizontalLayout_12.addWidget(self.Type)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_12.addItem(self.verticalSpacer_12)

        self.TypeInput = QComboBox(self.frame)
        self.TypeInput.setStyleSheet(u"background-color: #fff; color: black;")
        self.TypeInput.setObjectName(u"TypeInput")
        self.TypeInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        # Добавление опций в выпадающий список
        self.TypeInput.addItems(["ЗАО", "ООО", "ИП", "ОАО", "ПАО"])

        self.horizontalLayout_12.addWidget(self.TypeInput)

        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.Name = QLabel(self.frame)
        self.Name.setObjectName(u"Name")

        self.horizontalLayout_11.addWidget(self.Name)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_11.addItem(self.verticalSpacer_11)

        self.NameInput = QLineEdit(self.frame)
        self.NameInput.setStyleSheet(u"background-color: #fff; color: black;")
        self.NameInput.setObjectName(u"NameInput")

        self.horizontalLayout_11.addWidget(self.NameInput)

        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Address = QLabel(self.frame)
        self.Address.setObjectName(u"Address")

        self.horizontalLayout.addWidget(self.Address)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.AddressInput = QLineEdit(self.frame)
        self.AddressInput.setStyleSheet(u"background-color: #fff; color: black;")
        self.AddressInput.setObjectName(u"AddressInput")

        self.horizontalLayout.addWidget(self.AddressInput)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.INN = QLabel(self.frame)
        self.INN.setObjectName(u"INN")

        self.horizontalLayout_9.addWidget(self.INN)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_9.addItem(self.verticalSpacer_9)

        self.INNInput = QLineEdit(self.frame)
        self.INNInput.setStyleSheet(u"background-color: #fff; color: black;")
        self.INNInput.setObjectName(u"INNInput")

        self.horizontalLayout_9.addWidget(self.INNInput)

        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.BossName = QLabel(self.frame)
        self.BossName.setObjectName(u"BossName")

        self.horizontalLayout_10.addWidget(self.BossName)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_10.addItem(self.verticalSpacer_10)

        self.BossNameInput = QLineEdit(self.frame)
        self.BossNameInput.setStyleSheet(u"background-color: #fff; color: black;")
        self.BossNameInput.setObjectName(u"BossNameInput")

        self.horizontalLayout_10.addWidget(self.BossNameInput)

        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.PhoneNumber = QLabel(self.frame)
        self.PhoneNumber.setObjectName(u"PhoneNumber")

        self.horizontalLayout_15.addWidget(self.PhoneNumber)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_15.addItem(self.verticalSpacer_15)

        self.PhoneNumberInput = QLineEdit(self.frame)
        self.PhoneNumberInput.setStyleSheet(u"background-color: #fff; color: black;")
        self.PhoneNumberInput.setObjectName(u"PhoneNumberInput")

        self.horizontalLayout_15.addWidget(self.PhoneNumberInput)

        self.verticalLayout.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.Mail = QLabel(self.frame)
        self.Mail.setObjectName(u"Mail")

        self.horizontalLayout_14.addWidget(self.Mail)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_14.addItem(self.verticalSpacer_14)

        self.MailInput = QLineEdit(self.frame)
        self.MailInput.setStyleSheet(u"background-color: #fff; color: black;")
        self.MailInput.setObjectName(u"MailInput")

        self.horizontalLayout_14.addWidget(self.MailInput)

        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.Rank = QLabel(self.frame)
        self.Rank.setObjectName(u"Rank")

        self.horizontalLayout_13.addWidget(self.Rank)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_13.addItem(self.verticalSpacer_13)

        self.RankInput = QLineEdit(self.frame)
        self.RankInput.setStyleSheet(u"background-color: #fff; color: black;")
        self.RankInput.setObjectName(u"RankInput")

        self.horizontalLayout_13.addWidget(self.RankInput)

        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.CreateUpdateButton = QPushButton(self.frame)
        self.CreateUpdateButton.setObjectName(u"CreateUpdateButton")
        self.CreateUpdateButton.setStyleSheet(u"border: 1px solid black;\n"
                                              "background-color: #67BA80;\n"
                                              "")

        self.verticalLayout.addWidget(self.CreateUpdateButton)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border: 1px solid black;\n"
                                      "background-color: #67BA80;\n"
                                      "")

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(CreateUpdatePage)

        QMetaObject.connectSlotsByName(CreateUpdatePage)

    # setupUi

    def retranslateUi(self, CreateUpdatePage):
        CreateUpdatePage.setWindowTitle(QCoreApplication.translate("CreateUpdatePage", u"Form", None))
        self.label.setText(QCoreApplication.translate("CreateUpdatePage",
                                                      u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">\u041e\u043a\u043d\u043e \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f/\u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u043f\u0430\u0440\u0442\u043d\u0451\u0440\u0430</span></p></body></html>",
                                                      None))
        self.Type.setText(QCoreApplication.translate("CreateUpdatePage",
                                                     u"\u0422\u0438\u043f \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438:",
                                                     None))
        self.Name.setText(QCoreApplication.translate("CreateUpdatePage",
                                                     u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438:",
                                                     None))
        self.Address.setText(
            QCoreApplication.translate("CreateUpdatePage", u"\u042e\u0440. \u0430\u0434\u0440\u0435\u0441:", None))
        self.INN.setText(QCoreApplication.translate("CreateUpdatePage", u"\u0418\u041d\u041d:", None))
        self.BossName.setText(QCoreApplication.translate("CreateUpdatePage",
                                                         u"\u0418\u043c\u044f \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0430:",
                                                         None))
        self.PhoneNumber.setText(QCoreApplication.translate("CreateUpdatePage",
                                                            u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430:",
                                                            None))
        self.Mail.setText(
            QCoreApplication.translate("CreateUpdatePage", u"\u042d\u043b. \u043f\u043e\u0447\u0442\u0430:", None))
        self.Rank.setText(
            QCoreApplication.translate("CreateUpdatePage", u"\u0420\u0435\u0439\u0442\u0438\u043d\u0433:", None))
        self.CreateUpdateButton.setText(QCoreApplication.translate("CreateUpdatePage", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("CreateUpdatePage", u"BackButton", None))
    # retranslateUi
