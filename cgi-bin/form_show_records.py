import cgi
import sqlite3


db = sqlite3.connect('industrial_wood.db')
sql = db.cursor()
sql.execute(f"SELECT s.customer, t.type, c.count FROM customer_list c, sales s, types t WHERE c.customer_id = s.id and t.id = c.type_id")
lines =sql.fetchall()
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
            <div style="text-align: center;">
""")
print("<h1>Записи</h1>")
for line in lines:
    print(f'<p>{line[0]} | {line[1]} | {line[2]}')

print("""
        </div>
    </body>
""")
