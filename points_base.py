import sqlite3
import points_class

conn = sqlite3.connect('points.sqlite')
c = conn.cursor()

def add_user(identification_object,adress,geolocation,date):
    c.execute("INSERT INTO points (identification_object,adress,geolocation,date) VALUES (?,?,?,?)",(identification_object,adress,geolocation,date))
    conn.commit()