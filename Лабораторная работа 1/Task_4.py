users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
total = 0
unique = 0

describe = {
    "Общее количество" : total,
    "Уникальные посещения" : unique,
}

total = len(users)  # общее кол во посещений
unique = len(set(users))  # уникальные посетители

describe = {
    "Общее количество" : total,
    "Уникальные посещения" : unique,
}
print(describe)
