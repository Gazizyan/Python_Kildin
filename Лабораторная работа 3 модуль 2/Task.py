class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

    @property
    def pages(self) -> int:
        """
        Возвращает количество страниц
        """
        return self.pages

    @pages.setter
    def pages(self, pages_: int):
        """
        Устанавливает количество страниц
        """
        if not isinstance(pages_, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages_ <= 0:
            raise ValueError("Количество страниц не должно быть отрицательным")
        self.pages = pages_

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        self.name = name
        self.author = author
        self.duration = duration

    @property
    def duration(self) -> float:
        """
        Возвращает продолжительность книги
        """
        return self.duration

    @duration.setter
    def duration(self, duration_: float) -> None:
        """
        Устанавливает продолжительность книги
        """
        if not isinstance(duration_, float):
            raise TypeError("Продолжительность должна быть типа float")
        if duration_ <= 0:
            raise ValueError("Продолжительность не должна быть отрицательным")
        self.duration = duration_

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"
#