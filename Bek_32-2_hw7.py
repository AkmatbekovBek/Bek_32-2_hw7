import sqlite3



def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)

    except sqlite3.Error as e:
        print(e)
    return connection



def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

    except sqlite3.Error as e:
        print(e)


def insert_products(conn, products):
    sql = '''INSERT INTO Products
        (product_title, price, quantity)
        VALUES (?, ?, ?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()

    except sqlite3.Error as e:
        print(e)



def add_goods():
    insert_products(connection_to_db, ('Milk', 80, 10))
    insert_products(connection_to_db, ('Cheese', 35, 27))
    insert_products(connection_to_db, ('Meat', 500, 12))
    insert_products(connection_to_db, ('Soap', 40, 11))
    insert_products(connection_to_db, ('Eggs', 10, 60))
    insert_products(connection_to_db, ('Potato', 15, 45))
    insert_products(connection_to_db, ('Bread', 20, 30))
    insert_products(connection_to_db, ('Batteries', 5, 30))
    insert_products(connection_to_db, ('Toilet paper', 140, 22))
    insert_products(connection_to_db, ('Fishing rod', 840, 9))
    insert_products(connection_to_db, ('Scotch', 30, 55))
    insert_products(connection_to_db, ('Glue', 13, 21))
    insert_products(connection_to_db, ('Mousetrap', 75, 23))
    insert_products(connection_to_db, ('Headphones', 170, 45))
    insert_products(connection_to_db, ('SoapLiquid', 65, 38))



def change_the_quantity(conn, product):
    sql = '''UPDATE Products SET quantity = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()

    except sqlite3.Error as e:
        print(e)



def change_the_price(conn, product):
    sql = '''UPDATE Products SET price = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()

    except sqlite3.Error as e:
        print(e)



def delete_product(conn, id):
    sql = '''DELETE FROM Products WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()

    except sqlite3.Error as e:
        print(e)



def print_the_table(conn):
    sql = '''SELECT * FROM Products'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)

    except sqlite3.Error as e:
        print(e)



def price_up_to_100_soms(conn):
    sql = '''SELECT product_title, price, quantity FROM Products WHERE price <= 100'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)

    except sqlite3.Error as e:
        print(e)



def search_by_name(conn, product_title):
    sql = '''SELECT product_title, price, quantity FROM Products
             WHERE product_title LIKE ? '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (product_title,))

        conn.commit()

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)

    except sqlite3.Error as e:
        print(e)



sql_create_products_table = '''
CREATE TABLE Products (
id INTEGER PRIMARY KEY AUTO_INCREMENT,
product_title VARCHAR(200) NOT NULL,
price FLOAT(10, 2)  NOT NULL DEFAULT 0.0,
quantity INT NOT NULL DEFAULT 0)
'''


connection_to_db = create_connection('hw.db')
if connection_to_db is not None:
    print('Successfully connected to DB!')


# create_table(connection_to_db, sql_create_products_table)
# add_goods()
# change_the_quantity(connection_to_db, (99, 2))
# change_the_price(connection_to_db, (99, 2))
# delete_product(connection_to_db, (4))
# print_the_table(connection_to_db)
# price_up_to_100_soms(connection_to_db)
# search_by_name(connection_to_db, ('Meat'))


connection_to_db.close()

