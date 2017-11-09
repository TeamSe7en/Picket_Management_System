import person_base
import Person_class
import sqlite3

conn = sqlite3.connect('persons.sqlite')
c = conn.cursor()

person = Person_class.Person('Николай', 'Лацын', 'Какойтович', 'Бауманская')
person_base.add_user(person.name,person.surname,person.patronymic,person.stations)

c.execute('SELECT * FROM persons')
row = c.fetchone()

while row is not None:
    print("id: " + str(row[0]) + " Name: " + row[1] + " Surname: " + row[2] + " Patronymic: " + row[3] + " Station " + row[4])
    row = c.fetchone()

c.close()
conn.close()

