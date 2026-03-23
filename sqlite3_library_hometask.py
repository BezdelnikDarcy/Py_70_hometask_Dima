import sqlite3
from dataclasses import dataclass
from datetime import date

@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int = 0
    status: str = "available"

@dataclass
class Reader:
    id: int
    name: str
    age: int



class Library:

    def __init__(self, db_name = 'library.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                year INTEGER,
                status TEXT DEFAULT "available"
)
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS readers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS borrowed_books (
            reader_id INTEGER,
            book_id INTEGER,
            borrow_date TEXT,
            FOREIGN KEY(reader_id) REFERENCES readers(id),
            FOREIGN KEY(book_id) REFERENCES books(id),
            PRIMARY KEY(reader_id, book_id)
        )
        ''')

        self.conn.commit()


    def add_book(self, title: str, author: str, year: int):
        self.cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
        self.conn.commit()

    def add_reader(self, name: str, age: int):
        self.cursor.execute("INSERT INTO readers (name, age) VALUES (?, ?)", (name,age))
        self.conn.commit()

    def borrow_book(self, reader_id: int, book_id: int):
        borrow_time = date.today().isoformat()
        data = self.cursor.execute('''SELECT *
                                FROM borrowed_books
                                WHERE  book_id = ?          
                            ''', (book_id,))
        if data.fetchone():
            return f"Данная книга не доступна"
        else:
            self.cursor.execute(''' INSERT INTO borrowed_books (reader_id, book_id, borrow_date) VALUES (?, ?, ?)
            ''', (reader_id, book_id, borrow_time))
            self.cursor.execute('''UPDATE books
                                    SET status = "borrowed"
                                    WHERE id = ?''', (book_id,))
            self.conn.commit()
    def return_books(self, book_id: int):
        self.cursor.execute('''UPDATE books
                            SET status = 'available' WHERE id = ?
                            ''', (book_id,))
        self.cursor.execute(''' DELETE FROM borrowed_books
                            WHERE book_id = ?
                            ''', (book_id,))
        self.conn.commit()
    # def search_book(self, keyword: str):
    #     search_text = f"%{keyword}%"
    #     self.cursor.execute('''SELECT title, author,year
    #                                     FROM books
    #                                     WHERE title like ?
    #                                     OR author like ?
    #                                             ''', (search_text,search_text))
    #     return self.cursor.fetchall()
    def search_book(self, keyword: str):
        search_text = keyword.lower()
        found_books = []
        all_books = self.cursor.execute("SELECT id, title, author,year, status FROM books").fetchall()
        for i in range(len(all_books)):
            if search_text in all_books[i][1].lower() or search_text in all_books[i][2].lower():
                book = Book(
                    id=all_books[i][0],
                    title=all_books[i][1],
                    author=all_books[i][2],
                    year=all_books[i][3],
                    status=all_books[i][4]
                )
                found_books.append(book)
        return found_books
    def get_borrowed_books(self):
        self.cursor.execute('''SELECT books.id, books.title, books.author, books.year, books.status, readers.id, readers.name, readers.age, borrowed_books.borrow_date
                                FROM books
                                INNER JOIN borrowed_books ON books.id = borrowed_books.book_id
                                INNER JOIN readers ON readers.id = borrowed_books.reader_id
                                    ''')
        result = self.cursor.fetchall()

        borrowed = []
        for column in result:
            book = Book(id = column[0], title = column[1], author = column[2], year = column[3], status = column[4])
            reader = Reader(id = column[5], name = column[6], age = column[7])
            borrowed.append({
            "book": book,
            "reader": reader,
            "borrow_date": column[8]
            })
        return borrowed
    def get_statistics(self):
        self.cursor.execute('''SELECT 
                                COUNT(CASE WHEN status = "available" THEN 1 END) AS available,
                                COUNT(CASE WHEN status = "borrowed" THEN 1 END) AS borrowed
                                FROM books
                                ''')
        return self.cursor.fetchall()


lib = Library()

# Добавление книг
books = [
        ("Война и мир", "Лев Толстой", 1869),
        ("Преступление и наказание", "Фёдор Достоевский", 1866),
        ("Мастер и Маргарита", "Михаил Булгаков", 1967),
        ("1984", "Джордж Оруэлл", 1949),
        ("Убить пересмешника", "Харпер Ли", 1960),
        ("Три товарища", "Эрих Мария Ремарк", 1936)
    ]
# for title, author, year in books:
#     lib.add_book(title, author, year)
#

# qwery = '''DELETE FROM books
# WHERE id > ?'''
# id = 6
# with sqlite3.connect('library.db') as connection:
#     cursor = connection.cursor()
#     data  = cursor.execute(qwery,(id,))
#     connection.commit()

# conn = sqlite3.connect('library.db')
# cursor = conn.cursor()
# data = cursor.execute('''SELECT title, author, year FROM books''')
# for item in data:
#     print(item)

# Добавление читателей
readers = [
    ("Иван Петров", 25),
    ("Мария Иванова", 30),
    ("Алексей Сидоров", 22),
    ("Елена Смирнова", 28),
    ("Дмитрий Козлов", 35)
]

# for name, age in readers:
#     lib.add_reader(name, age)
# conn = sqlite3.connect('library.db')
# cursor = conn.cursor()
# data = cursor.execute('''SELECT name, age FROM readers''')
# for item in data:
#     print(item)

# Поиск книг

# search = list(input())
# for item in search:
#     results = lib.search_book(item)
#     if results:
#         for title, author, year in results:
#             print(f"{title} - {author} - {year}")
#     else:
#         print("Ничего не найдено")
found = lib.search_book("толстой")
for book in found:
    print(f"{book.title} - {book.author} - {book.year}")
# conn = sqlite3.connect('library.db')
# cursor = conn.cursor()
# data = cursor.execute('''SELECT title, author, year from books''')
# print(len(data.fetchall()))

#Выдача книг

# borrowed_books = [
#     (1, 3),
#     (2, 2),
#     (4, 6),
#     (3, 5)
# ]
# for reder_id, book_id in borrowed_books:
#     result = lib.borrow_book(reder_id, book_id)
#     if result == "Данная книга не доступна":
#         print(f"Книга ID{book_id} для читателя {reder_id} {result}")
#     else:
#         print(f"Книга ID {book_id} выдана читателю {reder_id}")

# Выданные книги

# borrowed = lib.get_borrowed_books()
#
# for item in borrowed:
#     print(f"{item['book'].title} у {item['reader'].name} выдана: {item['borrow_date']}")
# Статистика

# stats = lib.get_statistics()[0]
# print(f"Количество доступных книг - {stats[0]}, количество занятых книг - {stats[1]}")
#
# #Возврат книги
#
# lib.return_books(3)
# stats = lib.get_statistics()[0]
# print(f"Количество доступных книг - {stats[0]}, количество занятых книг - {stats[1]}")
#

