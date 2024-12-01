import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect("venn_data.db")
cursor = conn.cursor()

# Выполняем SQL-запрос для получения всех данных из таблицы
cursor.execute("SELECT * FROM venn_data")

# Извлекаем все записи и выводим их
rows = cursor.fetchall()
for row in rows:
    print(row)

# Закрываем соединение с базой данных
conn.close()
