# TODO Найдите количество книг, которое можно разместить на дискете
volume_dis = 1.44  # мб
lists = 100  # кол во листов
lines_on_list = 50  # строк на странице
symbols_on_line = 25  # символы в строке
bytes_on_symbol = 4

symbols_on_list = symbols_on_line * lines_on_list  # количество символов в странице
symbols_on_book = symbols_on_list * lists  # кол во символов в книге
volume_book = symbols_on_book * bytes_on_symbol  # объем одной книги равен кол ву символов в книге на 4 байта

volume_book /= (1024 * 1024)  # объем книги в мб

X = volume_dis // volume_book

print("Количество книг, помещающихся на дискету:", round(X))
