import re

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QMessageBox, QComboBox

from database.connection import session
from database.models.Partner import PartnerModel
from myui.widgets.CreateUpdatePage import Ui_CreateUpdatePage


class CreateUpdatePageWidget(QWidget, Ui_CreateUpdatePage):
    """
    Класс для виджета страницы создания/обновления партнёра.
    """

    def __init__(self, controller, mode: str, partner_id=None):
        super().__init__(controller)
        self.setupUi(self)

        self.mode = mode
        self.partner_id = partner_id
        self.session = session

        self.PhoneNumber.setText("Номер телефона (xxx xxx xx xx):")
        self.BossName.setText("ФИО директора:")

        # Установка текста кнопки в зависимости от режима
        if self.mode == "create":
            self.CreateUpdateButton.setText("Создать")
        elif self.mode == "update":
            self.CreateUpdateButton.setText("Обновить")
            self.load_partner_data()

        # Подключение обработчика нажатия кнопки
        self.CreateUpdateButton.clicked.connect(self.on_submit)
        from app import MainWindow

        self.pushButton.setText("Назад")
        self.pushButton.clicked.connect(lambda: MainWindow.switch_to_partner_page(controller))

    def load_partner_data(self):
        """
        Загружает данные партнёра из базы данных для режима "update".
        """
        if not self.partner_id:
            raise ValueError("partner_id должен быть указан в режиме 'update'.")

        # Получение данных партнёра
        partner = self.session.query(PartnerModel).filter_by(id=self.partner_id).first()
        if not partner:
            raise ValueError(f"Партнёр с ID {self.partner_id} не найден.")

        # Проверяем TypeInput
        print("TypeInput:", self.TypeInput)
        print("TypeInput type:", type(self.TypeInput))
        if not isinstance(self.TypeInput, QComboBox):
            raise TypeError("TypeInput должен быть экземпляром QComboBox.")

        # Проверяем данные QComboBox
        if self.TypeInput.count() == 0:
            print("TypeInput пуст. Добавляем тестовые элементы...")
            self.TypeInput.addItems(["ЗАО", "ООО", "ИП", "ОАО", "ПАО"])

        # Установка текста в QComboBox
        if self.TypeInput.findText(partner.type) != -1:
            self.TypeInput.setCurrentText(partner.type)
        else:
            print(f"Значение '{partner.type}' не найдено в QComboBox. Добавляем его.")
            self.TypeInput.addItem(partner.type)
            self.TypeInput.setCurrentText(partner.type)

        # Установка значений в остальные поля
        self.NameInput.setText(partner.company_name)
        self.AddressInput.setText(partner.address)
        self.INNInput.setText(partner.inn)
        self.BossNameInput.setText(partner.boss_name)
        self.PhoneNumberInput.setText(partner.phone_number or "")
        self.MailInput.setText(partner.mail or "")
        self.RankInput.setText(str(partner.rank))

    @Slot()
    def on_submit(self):
        try:
            data = {
                "type": self.TypeInput.currentText(),  # Используем currentText() для QComboBox
                "company_name": self.NameInput.text(),
                "address": self.AddressInput.text(),
                "inn": self.INNInput.text(),
                "boss_name": self.BossNameInput.text(),
                "phone_number": self.PhoneNumberInput.text() or None,
                "mail": self.MailInput.text() or None,
                "rank": self.RankInput.text(),
            }

            # Проверка типа компании
            partner_type = self.TypeInput.currentText()  # Используем currentText() для QComboBox
            if not re.fullmatch(r"^[A-Za-zА-Яа-я]{3}$", partner_type):
                QMessageBox.critical(self, "Ошибка", "Тип компании должен содержать ровно 3 буквы!")
                return

            # Проверка номера телефона
            phone_number = self.PhoneNumberInput.text()
            if not re.match(r"^\d{3} \d{3} \d{2} \d{2}$", phone_number):  # Проверка формата "444 222 33 11"
                QMessageBox.critical(
                    self,
                    "Ошибка",
                    "Номер телефона должен быть в формате: '444 222 33 11'!",
                )
                return

            # Проверка ИНН
            inn = self.INNInput.text()
            if not re.match(r"^\d{10}$", inn):  # Проверка, что ИНН состоит ровно из 10 цифр
                QMessageBox.critical(self, "Ошибка", "ИНН должен содержать ровно 10 цифр!")
                return

            # Проверка рейтинга
            rank = self.RankInput.text()
            if not rank.isdigit() or not (0 <= int(rank) <= 10):
                QMessageBox.critical(self, "Ошибка", "Неверный формат рейтинга!")
                return

            # Проверка почты
            mail = self.MailInput.text()
            if mail and "@" not in mail:
                QMessageBox.critical(self, "Ошибка", "Некорректный адрес электронной почты!")
                return

            # Проверка имени директора
            boss_name = self.BossNameInput.text()
            if any(char.isdigit() for char in boss_name):
                QMessageBox.critical(self, "Ошибка", "Имя директора не может содержать цифры!")
                return

            # Логика создания или обновления партнёра
            if self.mode == "create":
                new_partner = PartnerModel(**data)
                self.session.add(new_partner)
                self.session.commit()
                QMessageBox.information(self, "Успех", "Партнёр успешно создан!")
            elif self.mode == "update":
                partner = self.session.query(PartnerModel).filter_by(id=self.partner_id).first()
                if not partner:
                    raise ValueError(f"Партнёр с ID {self.partner_id} не найден.")
                for key, value in data.items():
                    setattr(partner, key, value)
                self.session.commit()
                QMessageBox.information(self, "Успех", "Данные партнёра успешно обновлены!")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка: {str(e)}")
