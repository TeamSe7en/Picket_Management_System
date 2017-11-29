import points_base
import points_class
import sqlite3

conn = sqlite3.connect('points.sqlite')
c = conn.cursor()

points = points_class.points('Магнит', 'Башиловская,30', '11111.2222.44', '02.11.2017')
points_base.add_user(points.identidication_object,points.adress,points.geolocation,points.date)

c.execute('SELECT * FROM points')
row = c.fetchone()

while row is not None:
    print("id: " + str(row[0]) + " Object: " + row[1] + " Adress: " + row[2] + " Geolocation: " + row[3] + " Date: " + row[4])
    row = c.fetchone()

c.close()
conn.close()