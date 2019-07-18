from django.db import models

# Create your models here.

class Category(models.Model) :
    id = models.IntegerField(primary_key=True)
    categorys = models.CharField(max_length = 20, unique = True)

    def __str__(self):
        return self.categorys



class Restaurant(models.Model) :
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 20, unique = True)
    categorys = models.CharField(max_length = 20)
    rate = models.FloatField()
    info = models.TextField()

    def __str__(self):
        return self.name