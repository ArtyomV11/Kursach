import sqlite3

conn = sqlite3.connect("venn_data.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES, check_same_thread=False)
cursor = conn.cursor()

try:
    cursor.execute("SELECT * FROM venn_data")
    rows = cursor.fetchall()
    for row in rows:
        print(tuple(str(item) for item in row))

except sqlite3.Error as e:
    print(f"Ошибка SQLite: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    conn.close()
