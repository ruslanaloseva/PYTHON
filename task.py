# Функция для поиска общих участников
def find_common_participants(group1, group2, separator=","):
    first_set = set(group1.split(separator))
    second_set = set(group2.split(separator))
    common = first_set & second_set
    return sorted(common)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверка работы функции с разделителем, отличным от запятой
result = find_common_participants(
    participants_first_group,
    participants_second_group,
    separator="|"
)