salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев
increase = 0.03  # Ежемесячный рост цен

money_capital = 0
current_spend = spend

for _ in range(months):
    # Нехватка средств в текущем месяце
    deficit = max(0, current_spend - salary)

    # Добавляем дефицит к подушке безопасности
    money_capital += deficit

    # Увеличиваем расходы на следующий месяц
    current_spend *= (1 + increase)

# Округляем до целого
money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)