from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Client(models.Model):
    name = models.CharField(max_length=200)
    sector = models.CharField(max_length=200)

class BoardMember(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
