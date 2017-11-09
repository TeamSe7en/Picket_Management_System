import sqlite3
import Person_class

conn = sqlite3.connect('persons.sqlite')
c = conn.cursor()

def add_user(user_name,user_surname,user_patronymic,user_stations):
    c.execute("INSERT INTO persons (Name,Surname,Patronymic,Station) VALUES (?,?,?,?)",(user_name,user_surname,user_patronymic,user_stations))
    conn.commit()



