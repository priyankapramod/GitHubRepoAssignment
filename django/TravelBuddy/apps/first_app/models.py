from django.db import models

# Create your models here.

class User(models.Model):
      # id = models.AutoField(primary_key=True)
      name = models.CharField(max_length=45)
      email = models.CharField(max_length=45)
      password = models.CharField(max_length=15)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)


class Destination(models.Model):
      # id = models.AutoField(primary_key=True)
      destination_name = models.CharField(max_length=45)
      # user_travelling = models.ManyToManyField(User)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)


class Trip(models.Model):
      # id = models.AutoField(primary_key=True)
      user_trip = models.ManyToManyField(User)
      dest_trip = models.ManyToManyField(Destination)
      description = models.CharField(max_length=15)
      date_from = models.DateField()
      date_to = models.DateField()
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)

