if __name__ == "__main__":
    class Car:
        """ Базовый класс автомобиль """
        def __init__(self, brand: str, model: str, color: str, year: int):
            """
            Создание и подготовка к работе объекта «Car»

            :param brand: Марка автомобиля
            :param model: Модель автомобиля
            :param color: Цвет автомобиля
            :param year: Год выпуска определенной модели автомобиля

            """
            if not isinstance(brand, str):
                raise TypeError("Название бренда указано неверно")
            if not isinstance(model, str):
                raise TypeError("Название модели указано неверно")
            if not isinstance(color, str):
                raise TypeError("Цвет указан неверно")
            if not isinstance(year, int):
                raise ValueError("Год указан неверно")

            self.label = label
            self.model = model
            self.color = color
            self.year = year

        def __str__(self) -> str:
            return f"Название марки автомобиля {self.brand}, модель {self.model}, цвет {self.color}, год выпуска {self.year}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r},year={self.year!r})"

    class TypeOfCar(Car):
        """ Базовый класс тип автомобиля """
        def __init__(self, type_: str) -> None:
            """
            Создание и подготовка к работе объекта "Автомобиль"
            :param type_: Тип автомобиля
            """
            super().__init__(brand='AUDI', model='RS 6', color='красный', year='2020')
            self.type_ = type_

        def type_(self) -> str:
            """Возвращает тип автомобиля(легковой/грузовой)"""
            return self.type_

        def __str__(self) -> str:
            return f"{super().__str__()}, {self.type_} тип"

        def __repr__(self) -> str:
            return f"Автомобиль {self.brand}, модель {self.model}, цвет {self.color}, год выпуска {self.year}, тип {self.type_}"

    pass
#