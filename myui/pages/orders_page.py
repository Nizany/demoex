from PySide6.QtWidgets import QWidget

# Импорт CRUD операций для работы с заказами и продуктами
from database.connection import session
from database.models.Order import OrderModel
from database.models.Product import ProductModel
# Импорт пользовательского интерфейса для карточки заказа
from myui.widgets.OrderCard import Ui_OrderCard
# Импорт пользовательского интерфейса для страницы заказов
from myui.widgets.OrdersPage import Ui_OrdersPage


class OrderCardWidget(QWidget, Ui_OrderCard):
    """
    Класс виджета для отображения информации о заказе.
    Представляет карточку, содержащую данные о продукте, количестве и дате создания заказа.
    """

    def __init__(self, product_name, quantity_of_products, date_of_create):
        super().__init__()
        self.setupUi(self)  # Инициализация пользовательского интерфейса
        self.setFixedHeight(130)  # Фиксированная высота карточки

        # Устанавливаем значения для отображения
        self.product_name.setText(product_name)
        self.quantity_of_products.setText("Количество заказанной продукции: " + quantity_of_products + " шт")
        self.date_of_create.setText("Дата создания заказа: " + date_of_create)


class OrderPageWidget(QWidget, Ui_OrdersPage):
    """
    Класс виджета для отображения страницы с заказами партнёра.
    Загружает заказы из базы данных и добавляет их в макет страницы.
    """

    def __init__(self, controller, partner_id):
        super().__init__()
        self.controller = controller

        self.setupUi(self)  #

        # Устанавливаем заголовок страницы
        self.Title.setText("Заказы")

        self.BackButton.setText("Назад")
        from app import MainWindow
        self.BackButton.clicked.connect(lambda: MainWindow.switch_to_partner_page(controller))

        # Получаем заказы для указанного партнёра и добавляем их на страницу
        for order in session.query(OrderModel).filter(OrderModel.fk_company_id == partner_id).all():
            custom_widget = OrderCardWidget(
                str(session.query(ProductModel.name).filter(ProductModel.id == order.fk_product_id).scalar()),  # Получаем название продукта
                str(order.quantity_of_products),  # Количество продукции
                str(order.date_of_create)  # Дата создания заказа
            )
            self.verticalLayout_4.addWidget(custom_widget)  # Добавляем виджет в вертикальный макет
