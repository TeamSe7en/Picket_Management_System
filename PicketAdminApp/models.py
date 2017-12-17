from django.db import models
from django.utils import timezone
from Allocation import metro_stations

with open('metro.dat', 'rb') as f:
    graph_metro = metro_stations.pickle.load(f)
    metro_list = list(graph_metro.vertices)
    STATION_LIST = [(metro,metro) for metro in metro_list]


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)


#class Metrostation(models.Model):
    #id = models.AutoField()
#    name = models.CharField(max_length=20, unique=True)

#    def __str__(self):
#        return self.name


class Person(models.Model):
    telegram_id = models.BigIntegerField(primary_key = True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, null = True, blank=True)
    station = models.CharField(max_length=50, null=True, blank=True, choices= STATION_LIST)

    def __str__(self):
        return str(self.surname)+' '+str(self.name)


class Place(models.Model):
    # широта, долгота
    latitude = models.FloatField()
    longitude = models.FloatField()
    shortname = models.CharField(max_length=20)
    metro = models.CharField(max_length=50, choices= STATION_LIST)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.shortname)


class Picket(models.Model):
    date = models.DateField(unique=True)
    text = models.TextField()
    place_list = models.FileField(null=True, blank=True)
    person_list = models.FileField(null=True, blank=True)
    places = models.ManyToManyField(Place,null=True, blank=True)
    persons = models.ManyToManyField(Person,null=True, blank=True)



    def __str__(self):
        return str(self.date)+str(self.places.all())#+str(self.persons)+str(self.places)


class Spot(models.Model):
    id = models.AutoField(primary_key=True)
    #person = models.ForeignKey(Person, db_constraint = False, null=True, blank=True)
    person = models.ForeignKey(Person, blank=True,null=True)
    #person = models.ManyToOneRel(Person)
    picket = models.ForeignKey(Picket)
    place = models.ForeignKey(Place,blank=True,null=True)
    fine = models.IntegerField(default=0)
    def __str__(self):
        if self.person == None:
            return str('Не назначено')+' / '+str(self.picket.date)+' / '+str(self.place.shortname)
        elif self.place == None:
            return str(self.person.surname)+' / '+str(self.picket.date)+' / '+str('Не назначено')
        else:
            return str(self.person.surname)+' / '+str(self.picket.date)+' / '+str(self.place.shortname)

        #return str(self.picket.date) + ' ' + self.place.shortname


class Task(models.Model):
    POLL_PICKET = 'poll_picket'
    ACCEPT_PICKET = 'accept_picket'
    INFO_PICKET = 'info_picket'
    GEO_PICKET = 'geo_picket'
    TASK_CHOICES = (
        (POLL_PICKET, "poll picket"),
        (ACCEPT_PICKET, "accept picket"),
        (INFO_PICKET , 'info picket'),
        (GEO_PICKET , 'geo picket')
    )
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=20,choices=TASK_CHOICES)
    status = models.BooleanField(default=True)
    date = models.DateField(null=False)
    data = models.CharField(max_length=1000,null=True, blank=True)
    def __str__(self):
        return str(self.name) + " "+ str(self.date)