money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0
capital = money_capital
current_spend = spend

while True:
    # Бюджет текущего месяца
    budget = capital + salary

    # Проверяем, хватает ли денег на текущие расходы
    if current_spend > budget:
        break

    # Тратим деньги
    capital = budget - current_spend
    months += 1

    # Увеличиваем расходы со следующего месяца
    current_spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", months)
