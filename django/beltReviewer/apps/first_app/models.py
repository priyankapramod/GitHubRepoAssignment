from django.db import models

# Create your models here.

class User(models.Model):
      # id = models.AutoField(primary_key=True)
      name = models.CharField(max_length=45)
      alias = models.CharField(max_length=45)
      email = models.CharField(max_length=45)
      password = models.CharField(max_length=15)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)

class Login(models.Model):
      email = models.CharField(max_length=45)
      password = models.CharField(max_length=15)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)

class Books(models.Model):
      # id = models.AutoField(primary_key=True)
      title = models.CharField(max_length=45)
      author = models.CharField(max_length=15)
      review = models.CharField(max_length=500)
      rating = models.CharField(max_length=15)
      user_of_book = models.ManyToManyField(User)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)

