BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]



class Book:
    def __init__(self, id: int, name: str, pages: int):
        """
        Cоздание и подготовка к работе объекта "Книга"
        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        if not isinstance(id, int):
            raise TypeError("Номер книги должен быть типа int")
        if id < 0:
            raise ValueError("Номер книги должен быть положительным")
        self.id = id

        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц не может быть меньше 0")
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
