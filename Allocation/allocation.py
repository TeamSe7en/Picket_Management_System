from Allocation import graph_class
from Allocation import metro_stations

from PicketAdminApp.models import Person
from PicketAdminApp.models import Place

with open('metro.dat', 'rb') as f:
    metro = metro_stations.pickle.load(f)

stations_list = []
persons_list = []
raspredelenie = {}
time = {}
minimum = ()

stations_list.append(Place('Дмитровская'))
stations_list.append(Place('Бауманская'))
stations_list.append(Place('Новоясеневская'))
stations_list.append(Place('Полежаевская'))

persons_list.append(Person(111,'Фили'))
persons_list.append(Person(222,'Речной вокзал'))
persons_list.append(Person(333,'Южная'))
persons_list.append(Person(444,'Пролетарская'))
persons_list.append(Person(555,'Бауманская'))

def allocation(persons_list_copy, places_list_copy):
    persons_list = list(persons_list_copy)
    places_list = list(places_list_copy)

    result = {}
    result['persons_excess'] = []
    result['places_excess'] = []
    result['matches'] = {}

    #урезаем список мест до количества людей
    while len(places_list) > len(persons_list):
        place = places_list.pop()
        result['places_excess'].append(place)

    for place in places_list:
        person_and_time = {}
        for person in persons_list:
            person_and_time[person] = graph_class.shortest_path(metro, person.station, place.metro)[1]#[1] - само время
        minimum = min(person_and_time.items(), key=lambda x: x[1])
        best_person = minimum[0]
        result['matches'][place] = best_person
        persons_list.remove(best_person)
        person_and_time.clear()

    while len(persons_list)>0:
        person = persons_list.pop()
        result['persons_excess'].append(person)

    return result



print(raspredelenie)


