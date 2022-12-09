import cgi
import sqlite3
import re


form = cgi.FieldStorage()
customer_name = form.getfirst("customer_name", "No value")
material_count = form.getfirst("material_count", "No value")
material_type = form.getfirst("material_type", "No value")
    
db = sqlite3.connect('industrial_wood.db')
sql = db.cursor()
sql.execute(f"SELECT id FROM sales WHERE customer = '{customer_name}'")
ans = sql.fetchall()

tpl1 = '^\d+$'
tpl2 = '^\w+$'

if re.match(tpl1, material_count) and re.match(tpl2, customer_name):
    answer = "Успешно обновлено!"
    if len(ans) > 0:
        customer_id = ans[0][0]
        sql.execute(f"UPDATE customer_list SET count = '{material_count}', type_id = '{material_type}' WHERE customer_id = '{customer_id}'")
        db.commit()
    else:
        answer = "Заказщик не найден x("
    
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
    print(f"<h1>{answer}</h1>")
    
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
