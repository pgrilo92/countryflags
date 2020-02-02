from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Language(models.Model):
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Flag(models.Model):
    country = models.CharField(max_length=100)
    capital_city = models.CharField(max_length=100)
    flag_img = models.URLField()
    continent = models.CharField(max_length=100)
    population = models.IntegerField()
    description = models.TextField(max_length=300)
    languages = models.ManyToManyField(Language)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.country

    def get_absolute_url(self):
        return reverse('detail', kwargs={'flag_id': self.id})

class President(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField('Presidency Start')
    end_date = models.DateField('Presidency End')
    flag = models.ForeignKey(Flag, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-end_date']
    