from django.db import models
from django.urls import reverse

class Flag(models.Model):
    country = models.CharField(max_length=100)
    capital_city = models.CharField(max_length=100)
    flag_img = models.URLField()
    continent = models.CharField(max_length=100)
    population = models.IntegerField()
    description = models.TextField(max_length=300)

    def __str_(self):
        return self.country

    def get_absolute_url(self):
        return reverse('detail', kwargs={'flag_id': self.id})

class President(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()