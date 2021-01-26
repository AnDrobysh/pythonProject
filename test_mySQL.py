import pymysql

# Подключиться к базе данных.
connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             db='test_shema')

cursor = connection.cursor()

cursor.execute('SELECT c.client_id, c.name, c.surname FROM test_shema.client c inner join test_shema.subcrubers sub on '
               'sub.client_id = c.client_id')
row = cursor.fetchone()
rest_of_rows = cursor.fetchall()
print(row)
print('_______')
print(rest_of_rows)
