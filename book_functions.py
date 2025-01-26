from pprint import pprint
from mysql.connector.cursor import MySQLCursor
def create_books_table(cursor):
    """
    Create a 'books' table in the database if it doesn't exist.
    """
    
    cursor.execute("create database if not exists Library")
    cursor.execute("use Library")
    cursor.execute("""create table if not exists Books(
                    id int auto_increment primary key,
                    title varchar(64) not null,
                    author varchar(64) not null,
                    published_year int not null,
                    genre varchar(64),
                    price int not null,
                    available boolean 
                    );
                   """)

def insert_book(cursor, title, author, published_year, genre, price):
    cursor.execute(f"""insert into Books(title, author, published_year, genre, price, available)
                        values ("{title}", "{author}", {published_year}, "{genre}", {price}, true); 
                   """)
    print("Maluot muvoffaqqiyatli qo`shildi!\n")

def show_all_books(cursor):
    cursor.execute("select * from Books")
    for i in cursor.fetchall():
        print(f"id: {i}")

def search_books_by_author_or_genre(cursor, search_type, search_value):
    cursor.execute(f"select id, {search_type} from Books where {search_type} = '{search_value}'")
    result = cursor.fetchall()
    for i in result:
        print(f"id:{i[0]}\n{search_type}: {i[1]}\n")

def update_book_price(cursor, book_id, new_price):
    if filter(lambda x: x[0] == book_id, cursor.fetchall()):
        cursor.execute(f"update books set price = {new_price} where id = {book_id} ")
        print("Ma`lumot muvovfaqqiyatli o`zgartirildi!\n")
        return 1
    else:
        return 0
    
def update_book_availability(cursor: MySQLCursor, book_id, available):
    cursor.execute("select * from Books")
    y = list(filter(lambda x: x[0] == book_id, cursor.fetchall()))
    if len(y) > 0:
        cursor.execute(f"""update Books 
                       set available = {available} 
                       where id = {book_id};
                        """)     

    else:
        print("Bu id da kitob yuq")
  
def delete_book(cursor: MySQLCursor, book_id: int)->None:
    cursor.execute("select id from Books")
    if list(map(lambda x: x[0], cursor.fetchall())).count(book_id):
        cursor.execute(f"delete from Books where id = {book_id}")
    else:
        print("Bunday id da kitob yuq")


def sort_books_by_year(cursor: MySQLCursor, order):
    while True:
        if order == '1' or order == '0':
            if order == '1':
                cursor.execute("select * from Books order by published_year asc")
                for i in cursor.fetchall():
                    print(f"Kitob nomi: {i[1]}\nKitob yaratilgan yil: {i[3]}\nAuthor: {i[2]}")
                break
            else:
                cursor.execute("select * from Books order by published_year DESC")
                for i in cursor.fetchall():
                    print(f"Kitob nomi: {i[1]}\nKitob yaratilgan yil: {i[3]}\nAuthor: {i[2]}")
                break
        else:
            print("Siz umuman boshqa buyrug kiritdingiz!\n")
 
def count_books(cursor: MySQLCursor):
    cursor.execute("SELECT COUNT(*) FROM books")
    count = cursor.fetchone()[0]
    print(f"Kitoblar soni: {count}\n")

def price_statistics(cursor):
    cursor.execute("SELECT MIN(price), MAX(price), AVG(price) FROM books")
    min_price, max_price, avg_price = cursor.fetchone()
    print(f"Min Price: {min_price}, Max Price: {max_price}, Avg Price: {avg_price:.2f}")

def menu():
    print("""
Buyruqlar:
Kitob yaratish -> 1
Barcha kitoblarni chiqarish ->2
Ma'lum bir shart bo'yicha qidiruv ->3
Kitob narxini yangilash ->4
Kitob mavjudligini o'zgartirish ->5
Kitobni o'chirish ->6
Yil bo'yicha saralash ->7
Jami kitoblar sonini chiqarish ->8
Narx bo'yicha statistikani chiqarish ->9
Kutubxonadan chiqish ->0\n
        """)
    