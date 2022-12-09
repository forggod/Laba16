import cgi
import sqlite3
import re


form = cgi.FieldStorage()
customer_name = form.getfirst("customer_name", "No value")
material_count = form.getfirst("material_count", "No value")
material_type = form.getfirst("material_type", "No value")

tpl1 = '^\d+$'
tpl2 = '^\w+$'

if re.match(tpl1, material_count) and re.match(tpl2, customer_name):

    db = sqlite3.connect('industrial_wood.db')
    sql = db.cursor()
    sql.execute(f"INSERT INTO sales(customer) VALUES ('{customer_name}')")
    db.commit()
    sql.execute(f"SELECT id FROM sales WHERE customer = '{customer_name}'")
    line =sql.fetchall()
    sql.execute(f"INSERT INTO customer_list(customer_id, type_id, count) VALUES ('{line[0][0]}', '{material_type}', '{material_count}')")
    db.commit()

    db.close()

    print("Content-type: text/html\n")
    print("""
        <!DOCTYPE HTML>
        <html>
            <head>
                <meta charset="utf-8">
                <title>Обработка данных форм</title>
            </head>
            <body>
    """)
    print("<h1>Записи сохранены!</h1>")
    print(f'<p>Заказщик:{customer_name}')
    print(f'<p>Тип материала:{material_type}')
    print(f'<p>Кол-во:{material_count}')

    print("""
        </body>
    """)
else:
    print("Content-type: text/html\n")
    print("""
        <!DOCTYPE HTML>
        <html>
            <head>
                <meta charset="utf-8">
                <title>Обработка данных форм</title>
            </head>
            <body>
    """)
    print("<h1>Ошибка!</h1>")
    print(f'<p>Неверное значение')

    print("""
        </body>
    """)
