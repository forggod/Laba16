import cgi
import sqlite3

# TODO: Проверку вводимых полей


form = cgi.FieldStorage()
customer_name = form.getfirst("customer_name", "No value")
    
db = sqlite3.connect('industrial_wood.db')
sql = db.cursor()
sql.execute(f"SELECT id FROM sales WHERE customer = '{customer_name}'")
ans = sql.fetchall()
answer = "Заказщик не найден x("
if len(ans) > 0 :
    sql.execute(f"DELETE FROM sales WHERE customer = '{customer_name}'")
    db.commit()
    sql.execute(f"DELETE FROM customer_list WHERE customer_id = '{ans[0][0]}'")
    db.commit()
    answer = "Заказщик успешно удален!"
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
