from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QFrame, QLabel, QVBoxLayout)


class Ui_OrderCard(object):
    def setupUi(self, OrderCard):
        if not OrderCard.objectName():
            OrderCard.setObjectName(u"OrderCard")
        OrderCard.resize(800, 130)
        OrderCard.setStyleSheet(u"background-color: #F4E8D3; color: #000; font-size: 18px; border: 2px solid black")

        # Устанавливаем вертикальный layout для OrderCard
        self.mainLayout = QVBoxLayout(OrderCard)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)  # Убираем отступы

        self.VLayout = QFrame(OrderCard)
        self.VLayout.setObjectName(u"VLayout")
        self.VLayout.setStyleSheet(u"border: 2px solid black;")  # Убедимся, что рамка есть
        from PySide6.QtWidgets import QSizePolicy

        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.VLayout.setSizePolicy(size_policy)

        self.verticalLayout_2 = QVBoxLayout(self.VLayout)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.product_name = QLabel(self.VLayout)
        self.product_name.setObjectName(u"product_name")
        self.product_name.setStyleSheet(u"border: none")

        self.verticalLayout_2.addWidget(self.product_name)

        self.quantity_of_products = QLabel(self.VLayout)
        self.quantity_of_products.setObjectName(u"quantity_of_products")
        self.quantity_of_products.setStyleSheet(u"border: none")

        self.verticalLayout_2.addWidget(self.quantity_of_products)

        self.date_of_create = QLabel(self.VLayout)
        self.date_of_create.setObjectName(u"date_of_create")
        self.date_of_create.setStyleSheet(u"border: none")

        self.verticalLayout_2.addWidget(self.date_of_create)

        self.mainLayout.addWidget(self.VLayout)  # Добавляем карточку в основной layout

        self.retranslateUi(OrderCard)
        QMetaObject.connectSlotsByName(OrderCard)

    def retranslateUi(self, OrderCard):
        OrderCard.setWindowTitle(QCoreApplication.translate("OrderCard", u"Form", None))
        self.product_name.setText(QCoreApplication.translate("OrderCard", u"product_name", None))
        self.quantity_of_products.setText(QCoreApplication.translate("OrderCard", u"quantity_of_products", None))
        self.date_of_create.setText(QCoreApplication.translate("OrderCard", u"date_of_create", None))
