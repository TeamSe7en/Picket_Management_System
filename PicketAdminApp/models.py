from django.db import models
from django.utils import timezone


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
    patronymic = models.CharField(max_length=20, null = True, blank=True)
    station = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.surname)+' '+str(self.name)


class Place(models.Model):
    # широта, долгота
    latitude = models.FloatField()
    longitude = models.FloatField()
    shortname = models.CharField(max_length=20)
    metro = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.shortname)


class Picket(models.Model):
    date = models.DateField(unique=True)
    text = models.TextField()
    place_list = models.FileField(null=True, blank=True)
    person_list = models.FileField(null=True, blank=True)
    places = []

    def __str__(self):
        return str(self.date)


class Spot(models.Model):
    #person = models.ForeignKey(Person, db_constraint = False, null=True, blank=True)
    person = models.ForeignKey(Person)
    #person = models.ManyToOneRel(Person)
    picket = models.ForeignKey(Picket)
    place = models.ForeignKey(Place)

    def __str__(self):
        return str(self.person.surname)+' '+str(self.picket.date)+' '+str(self.place.shortname)

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
    name = models.CharField(max_length=20,choices=TASK_CHOICES)
    status = models.BooleanField(default=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"