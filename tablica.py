import random
import pandas as pd

# Список возможных имен
names = ["Иванов", "Петров", "Сидоров", "Васильев", "Кузнецов", "Смирнов", "Попов", "Соколов", "Зайцев", "Михайлов"]

# Список возможных мест жительства
cities = ["Москва", "Санкт-Петербург", "Екатеринбург", "Новосибирск", "Челябинск", "Красноярск", "Нижний Новгород", "Казань", "Самара", "Омск"]

# Список возможных хобби
hobbies = ["Чтение", "Спорт", "Музыка", "Рисование", "Танцы", "Кино", "Игры", "Программирование", "Путешествия", "Кулинария"]

# Создание списка данных для DataFrame
data = []

# Генерация данных
for i in range(400):
    name = random.choice(names)
    birth_year = random.randint(1980, 2005)
    hobby = random.choice(hobbies)
    class_year = random.randint(9, 12)
    city = random.choice(cities)

    # Случайный выбор "Платное обучение" или "Бесплатное обучение"
    study_type = random.choice(["Платное обучение", "Бесплатное обучение"])

    # Создание соответствующих значений для столбцов
    paid_study = study_type == "Платное обучение"
    free_study = study_type == "Бесплатное обучение"

    driver_license = random.choice([True, False])
    smoking = random.choice([True, False])

    # Добавление строки в список
    data.append([name, birth_year, hobby, class_year, city, paid_study, free_study, driver_license, smoking])

# Создание DataFrame из списка
df = pd.DataFrame(data, columns=["Имя", "Год рождения", "Хобби", "Класс обучения", "Место жительства", "Платное обучение", "Бесплатное обучение", "Водительские права", "Курение"])

# Сохранение DataFrame в файл Excel
df.to_excel("Таблица.xlsx", index=False)