from database.connection import session
from database.models.Material import MaterialModel
from database.models.ProductType import ProductTypeModel


def calculate_material_amount(product_type_id: int, material_type_id: int, product_quantity: int,
                              param_length: float, param_width: float) -> int:
    """
    Рассчитывает количество необходимого материала для производства продукции с учётом брака.

    :param product_type_id: Идентификатор типа продукции (int).
    :param material_type_id: Идентификатор типа материала (int).
    :param product_quantity: Количество продукции (int).
    :param param_length: Длина продукции (float, положительный).
    :param param_width: Ширина продукции (float, положительный).
    :return: Количество необходимого материала (int) или -1, если данные некорректны.
    """
    try:
        # Проверка входных данных
        if not (isinstance(product_type_id, int) and isinstance(material_type_id,
                                                                int) and product_type_id > 0 and material_type_id > 0):
            return -1
        if not (isinstance(product_quantity, int) and product_quantity > 0):
            return -1
        if not (isinstance(param_length, (float, int)) and isinstance(param_width, (
                float, int)) and param_length > 0 and param_width > 0):
            return -1

        product_coefficient = session.query(ProductTypeModel.coefficient_of_product_type).filter(
            ProductTypeModel.id == product_type_id).scalar()
        defect_rate = session.query(MaterialModel.percentage_of_defective_material) \
            .filter(MaterialModel.id == material_type_id).scalar()

        if product_coefficient is None or defect_rate is None:
            return -1

        # Расчёт количества материала
        material_per_unit = param_length * param_width * product_coefficient
        total_material = material_per_unit * product_quantity
        total_material_with_defect = total_material * (1 + defect_rate / 100)

        return int(total_material_with_defect)

    except Exception as e:
        print(f"Ошибка: {e}")
        return -1


def console_interface(session: session):
    """
    Консольный интерфейс для расчёта количества материала.
    :param session: Сессия SQLAlchemy.
    """
    try:
        # Вывод доступных типов продукции
        print("Доступные типы продукции:")
        product_types = session.query(ProductTypeModel).all()
        if not product_types:
            print("Нет доступных типов продукции.")
            return

        for product in product_types:
            print(f"{product.id}: {product.type} (Коэффициент: {product.coefficient_of_product_type})")

        # Выбор типа продукции
        while True:
            product_type_id = input("Введите ID типа продукции: ")
            if product_type_id.isdigit() and int(product_type_id) in [product.id for product in product_types]:
                product_type_id = int(product_type_id)
                break
            print("Неверный ID типа продукции. Попробуйте ещё раз.")

        # Вывод доступных типов материалов
        print("Доступные типы материалов:")
        material_types = session.query(MaterialModel).all()
        if not material_types:
            print("Нет доступных типов материалов.")
            return

        for material in material_types:
            print(f"{material.id}: {material.type} (Процент брака: {material.percentage_of_defective_material}%)")

        # Выбор типа материала
        while True:
            material_type_id = input("Введите ID типа материала: ")
            if material_type_id.isdigit() and int(material_type_id) in [material.id for material in material_types]:
                material_type_id = int(material_type_id)
                break
            print("Неверный ID типа материала. Попробуйте ещё раз.")

        # Ввод остальных параметров
        while True:
            try:
                product_quantity = int(input("Введите количество продукции (целое число): "))
                param_length = float(input("Введите длину продукции (вещественное число): "))
                param_width = float(input("Введите ширину продукции (вещественное число): "))
                if product_quantity > 0 and param_length > 0 and param_width > 0:
                    break
                else:
                    print("Все значения должны быть положительными числами. Попробуйте ещё раз.")
            except ValueError:
                print(
                    "Некорректный ввод. Убедитесь, что количество целое, а параметры вещественные. Попробуйте ещё раз.")

        # Расчёт количества материала
        result = calculate_material_amount(product_type_id, material_type_id, product_quantity, param_length,
                                           param_width)

        # Вывод результата
        if result == -1:
            print("Произошла ошибка: проверьте корректность введённых данных.")
        else:
            print(f"Необходимое количество материала: {result}")

    except Exception as e:
        print(f"Ошибка в процессе работы программы: {e}")


console_interface(session)
