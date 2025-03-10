import sys

from PySide6.QtWidgets import QWidget, QMessageBox

from database.connection import session
from database.models.Order import OrderModel
from database.models.Partner import PartnerModel
from myui.widgets.PartnerCardWithButton import Ui_PartnerCardWithButton
from myui.widgets.PartnerPageWidget import Ui_PartnersPage


class PartnerPage(QWidget, Ui_PartnersPage):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller

        self.fill_scroll_area()

        self.pushButton.setText("Добавить партнера")
        self.pushButton.clicked.connect(lambda: controller.switch_to_create_page())
        self.pushButton_2.setText("Выйти")
        self.pushButton_2.clicked.connect(lambda: self.confirm_exit())

    def confirm_exit(self):
        # Подтверждение выхода
        reply = QMessageBox.warning(
            self,
            "Предупреждение",
            "Вы уверены, что хотите выйти?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            sys.exit(0)
        else:
            QMessageBox.information(
                self,
                "Продолжение работы",
                "Вы продолжаете работу в приложении."
            )

    def fill_scroll_area(self):
        # Добавление виджетов партнёров в область прокруткиыв
        for partner_model in session.query(PartnerModel).order_by(PartnerModel.id).all():
            custom_widget = PartnerCardWidget(self.controller, partner_model)
            self.verticalLayout_2.addWidget(custom_widget)


class PartnerCardWidget(QWidget, Ui_PartnerCardWithButton):
    def __init__(self, controller, partner_model):
        super().__init__()
        self.setupUi(self)
        self.setFixedHeight(180)
        self.central_widget = controller

        self.PartnerTypeAndName.setText(str(partner_model.type) + " | " + str(partner_model.company_name))
        self.BossName.setText(str(partner_model.boss_name))
        self.PhoneNumber.setText("+7 " + str(partner_model.phone_number))
        self.Rank.setText("Рейтинг " + str(partner_model.rank))

        # Вычисление и отображение процента скидки
        discount_percentage = calculation_of_discount_percentage(partner_model.id)
        self.DiscountPercentage.setText(str(discount_percentage) + "%")
        from app import MainWindow

        self.GetOrdersListButton.setText("Просмотреть заказы \n" + partner_model.company_name)
        self.GetOrdersListButton.clicked.connect(lambda: MainWindow.switch_to_order_page(controller, partner_model.id))

        self.BossName.clicked.connect(lambda: MainWindow.switch_to_update_page(controller, partner_model.id))
        self.PhoneNumber.clicked.connect(lambda: MainWindow.switch_to_update_page(controller, partner_model.id))
        self.Rank.clicked.connect(lambda: MainWindow.switch_to_update_page(controller, partner_model.id))
        self.DiscountPercentage.clicked.connect(lambda: MainWindow.switch_to_update_page(controller, partner_model.id))


def calculation_of_discount_percentage(partner_id: int) -> int:
    discount_percentage = 0
    total_amount_of_order = 0

    for order in session.query(OrderModel).filter(OrderModel.fk_company_id == partner_id).all():
        total_amount_of_order += order.quantity_of_products

    if 0 < total_amount_of_order < 1000:
        discount_percentage = 0
    elif 10000 < total_amount_of_order < 50000:
        discount_percentage = 5
    elif 50000 < total_amount_of_order < 300000:
        discount_percentage = 10
    elif 300000 < total_amount_of_order:
        discount_percentage = 15

    return discount_percentage
