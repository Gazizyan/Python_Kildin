import doctest  # TODO Написать 3 класса с документацией и аннотацией типов
class Factory:
    def __init__(self, model, year, speed=0):
        """
        Создание и подготовка к работе объекта «Завод/производство»
        :param model: модель машины выпускаемой на данном заводе
        :param year: год выпуска
        :param speed: количество выпускаемых машин в день (1 конвейер выпускает 1 машину в день)
        :param conveyor: максимальное количество конвееров

        Пример:
        >>> factory = Factory('Volkswagen Golf', 2015, 5, 10)
        """
        self.model = model
        self.year = year
        self.speed = speed
        self.conveyor = conveyor

    def organization(self, update):
        """
        Приобретение новых конвейеров
        :param update: количество новых конвееров
        :return: значение выпускаемых машин в день
        """
        if not isinstance(update, int):
            raise TypeError('Количество конвееров должно быть типа int')
        if update < 0:
            raise ValueError('Количество конвейров должно быть неотрицательным числом')
        if self.speed + update > self.conveyor:
            raise ValueError('Количество конвейеров превышает максимальное количество')

        self.speed += update

    def size_factory(self):
        """
        Функция определяющая большое ли производство
        :return: Масштабность
        """
        if self.speed == 0:
            return 'Нет завода'
        elif self.speed <= 9:
            return 'Маленькое производство'
        else:
            return 'Большое производство'


class Glasses:
    def __init__(self, material: str, frame_color: str, diopters: float):
        """
        Создание объекта "Очки"
        :param material: Материал
        :param frame_color: Цвет оправы
        :param diopters: Величина диоптрий
        Примеры:
        >>> glasses = Glasses('Стекло прозрачное', 'Черный цвет', -2.5)
        """
        if not isinstance(material, str):
            raise TypeError("Материал не выбран")
        if ('Стекло' or 'Пластик') not in material:
            raise ValueError("Неверно задан материал")
        self.material = material

        if not isinstance(frame_color, str):
            raise TypeError("Цвет оправы не выбран")
        if 'цвет' not in frame_color:
            raise ValueError("Неверный параметр")
        self.frame_color = frame_color

        if not isinstance(diopters, (int, float)):
            raise TypeError("Неверно выбраны линзы")
        self.diopters = diopters

    def choose_glasses(self) -> bool:
        """
        Функция, определяющая нужны ли вам очки
        :return: Нужны ли очки
        Примеры:
        >>> glasses = Glasses('Стекло прозрачное', 'Черный цвет', -2.5)
        >>> glasses.choose_glasses()
        True
        """
        if self.diopters != 1:
            return True

    def type_of_violation(self) -> str:
        """
        Функция, определяющая дальнозоркость у вас или близорукость
        :return: Диагноз
        Примеры:
        >>> glasses = Glasses('Стекло прозрачное', 'Черный цвет', -2.5)
        >>> glasses.type_of_violation()
        'Близорукость'
        """
        if self.diopters < 0:
            return 'Близорукость'
        elif self.diopters > 0:
            return 'Дальнозоркость'

class Laptop:
    def __init__(self, material: str, volume: int, screen_diagonal: int):
        """
        Создание объекта Ноутбук
        :param material: Материал
        :param volume: Объем ОЗУ
        :param screen_diagonal: Диагональ экрана

        Пример:
        >>> laptop = Laptop('Металл', 8, 15)
        """
        if not isinstance(material, str):
            raise TypeError("Материал не выбран")
        if ('Металл' or 'Пластик') not in material:
            raise ValueError("Неверно задан материал")
        self.material = material

    def volume_upd(self, volume_update: int) -> str:
        """
        Функция которая увеличивает объем ОЗУ на ноутбуке
        :param volume_update: количество добавляемого ОЗУ
        :return: Объем
        """
        if not isinstance(volume_update, int):
            raise TypeError('Объем ОЗУ должно быть типа int')
        if volume_update < 0:
            raise ValueError('Объем ОЗУ должно быть неотрицательным числом')

        self.volume += volume_update

    def coolest(self):
        """
        функция определяющая как хорошо ноутбук отводит тепло
        :return: Хорошо или плохо

        Пример:
        >>> laptop = Laptop('Металл', 8, 15)
        >>> laptop.coolest()
        'Хорошо отводит тепло'
        """

        if self.material == 'Металл':
            return 'Хорошо отводит тепло'
        else:
            return 'Плохо отводит тепло'


if __name__ == "__main__":
    doctest.testmod()
    pass
