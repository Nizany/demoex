import sys

from PySide6.QtCore import QTranslator, QLibraryInfo
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from ui.pages.create_update import CreateUpdatePageWidget
from ui.pages.orders_page import OrderPageWidget
from ui.pages.partner_page import PartnerPage


class MainWindow(QMainWindow):
    """
    Класс основного окна приложения
    """

    def __init__(self):
        super().__init__()
        # Устанавливаем заголовок окна
        self.setWindowTitle("Партнеры")
        # Устанавливаем размер и положение окна
        self.setGeometry(400, 400, 980, 500)

        # Создаём виджет для страницы партнёров

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        # self.partner_page_widget = PartnerPageWidget()
        self.partner_page = PartnerPage(self)
        self.central_widget.addWidget(self.partner_page)
        self.order_page = None

    def switch_to_update_page(self, partner_id: int):
        """
        Статический метод для переключения на страницу обновления.
        """
        self.setWindowTitle("Обновление заявки")

        self.order_page = CreateUpdatePageWidget(self, "update", partner_id)
        self.central_widget.addWidget(self.order_page)

        self.central_widget.setCurrentWidget(self.order_page)

    def switch_to_create_page(self):
        self.setWindowTitle("Создание заявки")

        self.order_page = CreateUpdatePageWidget(self, "create")
        self.central_widget.addWidget(self.order_page)

        self.central_widget.setCurrentWidget(self.order_page)

    def switch_to_order_page(self, partner_id: int):
        """
        Статический метод для переключения на страницу заказов.
        """
        self.setWindowTitle("Заказы")

        self.order_page = OrderPageWidget(self, partner_id)
        self.central_widget.addWidget(self.order_page)

        self.central_widget.setCurrentWidget(self.order_page)

    @staticmethod
    def switch_to_partner_page(self):
        """
        Статический метод для переключения на страницу партнёров.
        """
        self.setWindowTitle("Партнеры")

        self.new_partner_page = PartnerPage(self)
        self.central_widget.addWidget(self.new_partner_page)
        self.central_widget.setCurrentWidget(self.new_partner_page)


# Основная точка входа в приложение
if __name__ == "__main__":
    # Создаём приложение
    app = QApplication(sys.argv)
    # Создаём главное окно приложения
    translator = QTranslator()
    translator.load("qtbase_ru", QLibraryInfo.path(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)
    window = MainWindow()
    # Устанавливаем иконку приложения
    window.setWindowIcon(QPixmap("ui/icons/Master_pol.ico"))
    # Отображаем главное окно
    window.show()
    # Запускаем цикл обработки событий приложения
    app.exec()
