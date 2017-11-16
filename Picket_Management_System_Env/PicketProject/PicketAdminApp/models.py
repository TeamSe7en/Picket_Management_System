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


class Metrostation(models.Model):
    #id = models.AutoField()
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    telegram_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20, null = True, blank=True)
    station = models.ForeignKey(Metrostation, null=True, blank=True)

    def __str__(self):
        return self.surname+self.name+self.patronymic


class Place(models.Model):
    #id = models.AutoField()
    # широта, долгота
    latitude = models.FloatField()
    longitude = models.FloatField()
    shortname = models.CharField(max_length=20)
    metro = models.ForeignKey(Metrostation)
    description = models.TextField()

    def __str__(self):
        return self.shortname


class Picket(models.Model):
    #id = models.AutoField()
    date = models.DateField(unique=True)
    text = models.TextField()

    def __str__(self):
        return self.date


class Spot(models.Model):
    #id = models.AutoField()
    person = models.ForeignKey(Person)
    date = models.DateField()
    place = models.ForeignKey(Place)

    def __str__(self):
        return self.date+self.place+self.person