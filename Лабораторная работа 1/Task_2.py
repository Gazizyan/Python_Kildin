list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
total_players = len(list_players)
center_players = total_players // 2

team_1 = list_players[:center_players]
team_2 = list_players[center_players:]

print(team_1)
print(team_2)
