import pandas as pd
from matplotlib_venn import venn2, venn3
from venn import venn  # Для диаграмм с 4 и 5 категориями
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages  # Для сохранения в единый PDF файл
import sqlite3  # Для работы с базой данных

# Подключение к базе данных SQLite (или создание новой базы данных)
conn = sqlite3.connect("venn_data.db")
cursor = conn.cursor()

# Создаем таблицу для хранения данных категорий, если она еще не создана
cursor.execute('''
    CREATE TABLE IF NOT EXISTS venn_data (
        category_name TEXT,
        item_id INTEGER
    )
''')
conn.commit()

# Загружаем данные из Excel файла
df = pd.read_excel("Tablica.xlsx")

# Создаем список категорий для диаграмм Венна
categories = ["Платное обучение", "Бесплатное обучение", "Водительские права", "Курение", "Прививки", "Домашние животные"]

# Создаем список для хранения данных по каждой категории и добавляем их в базу данных
data = []
for category in categories:
    items = set(df[df[category] == True].index)
    data.append(items)
    # Записываем данные в базу
    cursor.executemany(
        "INSERT INTO venn_data (category_name, item_id) VALUES (?, ?)",
        [(category, item) for item in items]
    )
conn.commit()

# Открываем PDF файл для сохранения всех диаграмм
with PdfPages("venn_diagrams_all_categories.pdf") as pdf:
    # Создание диаграмм для двух категорий и сохранение их в PDF
    fig, axes = plt.subplots(3, 3, figsize=(15, 15))  # Устанавливаем сетку 3x3
    plt.subplots_adjust(hspace=0.4, wspace=0.4)  # Настраиваем расстояние между диаграммами

    venn_pairs = [
        (data[0], data[1], "Платное vs Бесплатное обучение", "Платное", "Бесплатное"),
        (data[0], data[2], "Платное обучение vs Водительские права", "Платное", "Права"),
        (data[0], data[3], "Платное обучение vs Курение", "Платное", "Курение"),
        (data[0], data[4], "Платное обучение vs Прививки", "Платное", "Прививки"),
        (data[0], data[5], "Платное обучение vs Домашние животные", "Платное", "Животные"),
        (data[1], data[2], "Бесплатное обучение vs Водительские права", "Бесплатное", "Права"),
        (data[1], data[3], "Бесплатное обучение vs Курение", "Бесплатное", "Курение"),
        (data[1], data[4], "Бесплатное обучение vs Прививки", "Бесплатное", "Прививки"),
        (data[1], data[5], "Бесплатное обучение vs Домашние животные", "Бесплатное", "Животные")
    ]

    for i, (set1, set2, title, label1, label2) in enumerate(venn_pairs):
        ax = axes[i // 3, i % 3]
        ax.set_title(title, fontsize=12)
        venn2(subsets=(set1, set2), set_labels=(label1, label2), ax=ax)

    # Добавляем страницу с диаграммами для двух категорий в PDF
    pdf.savefig(fig)
    plt.close(fig)

    # Создание диаграммы Венна для трех категорий и добавление в PDF
    fig_3 = plt.figure(figsize=(10, 5))
    ax1 = fig_3.add_subplot(1, 1, 1)
    ax1.set_title("Диаграмма Венна: Платное обучение, Курение и Прививки", fontsize=12)
    venn3(subsets=(data[0], data[3], data[4]), set_labels=("Платное", "Курение", "Прививки"), ax=ax1)

    pdf.savefig(fig_3)
    plt.close(fig_3)

    # Создание диаграммы Венна для четырех категорий и добавление в PDF
    fig_4 = plt.figure(figsize=(10, 5))
    ax2 = fig_4.add_subplot(1, 1, 1)
    ax2.set_title("Диаграмма Венна с 4 категориями", fontsize=12)
    venn_data_4 = {'Платное': data[0], 'Курение': data[3], 'Прививки': data[4], 'Права': data[2]}
    venn(venn_data_4, ax=ax2)

    pdf.savefig(fig_4)
    plt.close(fig_4)

# Закрываем соединение с базой данных
conn.close()

# Все диаграммы теперь сохранены в единый PDF файл "venn_diagrams_all_categories.pdf"
