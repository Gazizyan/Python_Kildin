money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
number_month = 0

while money_capital > 0:
    money_capital += (salary - spend)
    spend *= (1 + increase)
    print(money_capital)
    if money_capital > 0:
        number_month += 1
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", number_month)
