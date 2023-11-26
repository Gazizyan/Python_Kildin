import json
def calculate_sum_of_products(data_json):
    total_sum = 0.0

    for entry in data_json:     # Расчет значения из файла
        score = entry.get("score", 0)
        weight = entry.get("weight", 0)
        product = score * weight
        total_sum += product

    return round(total_sum, 3)

with open('input.json', 'r') as f:    # Чтение данных из файла
    data_json = json.load(f)

# Вызов функции и вывод результата
result = calculate_sum_of_products(data_json)
print(result)
