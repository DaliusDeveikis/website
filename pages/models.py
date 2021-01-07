from django.db import models
from stdimage import StdImageField


class Intro(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    citation = models.TextField(max_length=200)
    image = StdImageField(upload_to='photos/%Y/%m/%d/', blank=True, variations={
        'large': (600, 400),
        'thumbnail': (100, 100, True),
        'medium': (300, 200),
    }, delete_orphans=True)
    is_active = models.BooleanField(default=False)


    def represent(self):
        return str(self.name) + " " + str(self.surname) + " - " + str(self.profession)



class Service(models.Model):
    title = models.CharField(max_length=100)
    image = StdImageField(upload_to='photos/%Y/%m/%d/', blank=True, variations={
        'large': (600, 400),
        'thumbnail': (100, 100, True),
        'medium': (300, 200),
    }, delete_orphans=True)
    description = models.CharField(max_length=300)
    advantage1 = models.CharField(max_length=50, default='')
    advantage2 = models.CharField(max_length=50, default='')
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

