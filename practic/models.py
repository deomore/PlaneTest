from django.db import models


class Roles(models.Model):
    role = models.CharField()


class User(models.Model):
    login = models.CharField()
    password = models.CharField()
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)


class Author(models.Model):
    nickname = models.CharField()
    desc = models.CharField()
    birthday = models.DateField()


class Genres(models.Model):
    genre = models.CharField()


class Books(models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.CharField
    release_date = models.DateField()
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
