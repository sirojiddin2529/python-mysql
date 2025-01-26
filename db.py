from book_functions import create_books_table, insert_book, show_all_books, search_books_by_author_or_genre, update_book_price, update_book_availability, delete_book, sort_books_by_year, count_books, price_statistics, menu

import mysql.connector
import login
from pprint import pprint
try:
    connection = mysql.connector.connect(
        host=login.host,
        user=login.user,
        password=login.password,
        port=login.port
    )
    cursor = connection.cursor()
    create_books_table(cursor)
    while True:
        menu()
        number = input("Buyruqni kiriting: ")
        if number == '1':
    
            while True:
                title = input("Kitobni nomini kiriting: ")
                author = input("Kitobni authorini kiriting: ")
                published_year = int(input("Kitobni yaratilgan yili: "))
                genre = input("Kitobni janrini kiriting: ")
                price = int(input("kitobni narxini kiriting: "))
                
                insert_book(cursor, title, author, published_year, genre, price)
                x = input("Yana ma`lumot qo`shmoqchi bo`lsangiz 1 ni bosing, aks holda hohlagan bilgini: ")
                if x != '1':
                    connection.commit()
                    break
        elif number == '2':
            
            show_all_books(cursor)
        elif number == '3':
            
            print("author yoki genre ni kiriting")
            search_type = input("Qidiruv turini(yuqoridagilardan biri) kiriting: ")
            search_value = input("Qidiruv turi qiymatini kiriting: ")
            search_books_by_author_or_genre(cursor, search_type, search_value)
        elif number == '4':
        
            while True:
                id_book = int(input("O`zgartirmoqchi bo`lgan kitob id sini kiriting: "))
                new_price = int(input("Yangi narxni kiriting: "))
                if update_book_price(cursor, id_book, new_price):
                    new_book = input("Yana yangi ma`lumot qo`shmoqchi bo`lsangiz 1 ni bosing aks holda ixtiyoriy bilgini: ")
                    connection.commit()
                    if new_book != '1':
                        break
                else:
                    print("siz kiritgan id bo`yicha kitob mavjud emas, iltimos qaytadan kiriting\n")
        elif number == '5':
            
            book_id = int(input("Id bo`yicha kitobni so`rang: "))
            available = input("Kitobni mavjud qilmoqchi bo`lsangiz 1, aks holda 0 ni bosing: ")
            update_book_availability(cursor, book_id, available) 
            connection.commit()
        elif number == '6':
        
            book_id = int(input("Qaysi id dagi kitobni o`chirmoqchisiz: "))
            delete_book(cursor, book_id)
        elif number == '7':
            
            order = input("Agar ASC bo`yicha bo`lsa 1, aks holda 0 kiriting: ")
            sort_books_by_year(cursor, order)
        elif number == '8':
            
            count_books(cursor)
        elif number == '9':
    
            price_statistics(cursor)
        elif number == '0':
            print("kutubxonamizga tashrif buyurdingiz \n")
            exit()
        else: 
            print("\nSiz noto'g'ri buyruq kiritdingiz\n")

except:
    print("xato")
    