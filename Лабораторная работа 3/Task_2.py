# TODO Напишите функцию find_common_participants
def find_common_perticipants(participants_first_group, participants_second_group, separator=','):
    # переведем список в множество и разделяем это множество при помощи разделителем
    participants_first_group = set(participants_first_group.split(separator))
    participants_second_group = set(participants_second_group.split(separator))

    # находим пересекающиеся элементы в обеих группах
    common_participants = participants_first_group.intersection(participants_second_group)
    # создаем список из множества и сортируем
    common_participants = sorted(list(common_participants))

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_perticipants(participants_first_group, participants_second_group, separator='|')
print("Общие участники:", common_participants)
# TODO Провеьте работу функции с разделителем отличным от запятой

""" 
при запуске задания через (правую клавишу мыши) RUN task выдает ответ: Общие участники: ['Петров', 'Сидоров']
но при проверке задания через check, выдает такое сообщение: Failed to launch checking. For more information, see the 
Troubleshooting guide
и задание не проверяется
"""
