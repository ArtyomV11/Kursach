import os
import pymongo
from bson import Binary


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pdf_database"]
collection = db["pdf_files"]


folder_path = r"data_PDF/"

def upload_pdfs_to_mongodb(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            
            # Чтение PDF файла в бинарном формате
            with open(file_path, "rb") as file:
                pdf_data = file.read()
            
            # Сохранение PDF в MongoDB
            file_document = {
                "filename": filename,
                "file_data": Binary(pdf_data)
            }
            
            # Вставляем документ в коллекцию
            collection.insert_one(file_document)
            print(f"Загружен файл: {filename}")

# Запуск функции загрузки PDF файлов
upload_pdfs_to_mongodb(folder_path)
