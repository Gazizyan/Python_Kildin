# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def csv_to_json(input_filename, output_filename):
    with open(input_filename, 'r') as csv_file:     # читаем csv файл
        csv_reader = csv.reader(csv_file)

        headers = next(csv_reader)      # считываем 1 строчку, эти значения будут заголовками
        data = []       # создаем список

        for row in csv_reader:
            # создаем список в котором заголовки - ключи, значения - значения в строке
            dict = {header: value for header, value in zip(headers, row)}
            data.append(dict)       # добавляем в список

    json_data = json.dumps(data, indent=4)  # # cериализуем данные в JSON

    with open(output_filename, 'w') as json_file:
        json_file.write(json_data)

def task() -> None:
    csv_to_json(INPUT_FILENAME, OUTPUT_FILENAME)

if __name__ == '__main__':
    # Вызываем функцию task() для выполнения конвертации
    task()

    # Выводим содержимое созданного JSON файла
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
