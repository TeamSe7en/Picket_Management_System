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
        return self.title


#class Metrostation(models.Model):
    #id = models.AutoField()
#    name = models.CharField(max_length=20, unique=True)

#    def __str__(self):
#        return self.name


class Person(models.Model):
    telegram_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20, null = True, blank=True)
    station = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.surname+' '+self.name+' '+self.patronymic


class Place(models.Model):
    # широта, долгота
    latitude = models.FloatField()
    longitude = models.FloatField()
    shortname = models.CharField(max_length=20)
    metro = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.shortname


class Picket(models.Model):
    date = models.DateField(unique=True)
    text = models.TextField()
    place_list = models.FileField()

    def __str__(self):
        return str(self.date)


class Spot(models.Model):
    person = models.ForeignKey(Person)
    picket = models.ForeignKey(Picket)
    place = models.ForeignKey(Place)

    def __str__(self):
        return self.person.surname+' '+str(self.picket.date)+' '+self.place.shortname
