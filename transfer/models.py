from django.db import models


# Create your models here.
class Market(models.Model):
    CATEGORIES = (
        ('legend', 'legend'),
        ('superstar', 'superstar'),
        ('young', 'young'),
        ('prof', 'prof'),
        ('quick', 'quick'),
        ('strong', 'strong')
    )

    pcategory = (
        ('fwd', 'fwd'),
        ('mfd', 'mfd'),
        ('def', 'def'),
        ('gk', 'gk')
    )

    cskills = (
        ('💷💷💷💷💷💷💷💷💷💷💷💷💷', '💷💷💷💷💷💷💷💷💷💷💷💷💷'),
        ('💷💷💷💷💷💷💷💷💷💷💷💷', '💷💷💷💷💷💷💷💷💷💷💷💷'),
        ('💷💷💷💷💷💷💷💷💷💷💷', '💷💷💷💷💷💷💷💷💷💷💷'),
        ('💷💷💷💷💷💷💷💷💷💷', '💷💷💷💷💷💷💷💷💷💷'),
        ('💷💷💷💷💷💷💷💷💷', '💷💷💷💷💷💷💷💷💷'),
        ('💷💷💷💷💷💷💷💷', '💷💷💷💷💷💷💷💷'),
        ('💷💷💷💷💷💷💷', '💷💷💷💷💷💷💷'),
        ('💷💷💷💷💷💷', '💷💷💷💷💷💷'),
        ('💷💷💷💷💷', '💷💷💷💷💷'),
        ('💷💷💷💷', '💷💷💷💷'),
        ('💷💷💷', '💷💷💷'),
        ('💷💷', '💷💷'),
        ('💷', '💷')
     )
    name = models.CharField(max_length=255)
    position = models.CharField(
        max_length=20,
        choices=pcategory
    )
    age = models.IntegerField()
    skills = models.CharField(
        default='💷',
        max_length=200,
        choices=cskills
    )
    experience = models.CharField(
        max_length=20,
        choices=CATEGORIES
    )
    date_buyed = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['position','-skills']

    def __str__(self):
        return self.name


class Myteam(models.Model):
    CATEGORIES = (
        ('legend', 'legend'),
        ('superstar', 'superstar'),
        ('young', 'young'),
        ('prof', 'prof'),
        ('quick', 'quick'),
        ('strong', 'strong')
    )

    pcategory = (
        ('fwd', 'fwd'),
        ('mfd', 'mfd'),
        ('def', 'def'),
        ('gk', 'gk')
    )

    cskills = (
        ('💷💷💷💷💷💷💷💷💷💷💷💷💷', '💷💷💷💷💷💷💷💷💷💷💷💷💷'),
        ('💷💷💷💷💷💷💷💷💷💷💷💷', '💷💷💷💷💷💷💷💷💷💷💷💷'),
        ('💷💷💷💷💷💷💷💷💷💷💷', '💷💷💷💷💷💷💷💷💷💷💷'),
        ('💷💷💷💷💷💷💷💷💷💷', '💷💷💷💷💷💷💷💷💷💷'),
        ('💷💷💷💷💷💷💷💷💷', '💷💷💷💷💷💷💷💷💷'),
        ('💷💷💷💷💷💷💷💷', '💷💷💷💷💷💷💷💷'),
        ('💷💷💷💷💷💷💷', '💷💷💷💷💷💷💷'),
        ('💷💷💷💷💷💷', '💷💷💷💷💷💷'),
        ('💷💷💷💷💷', '💷💷💷💷💷'),
        ('💷💷💷💷', '💷💷💷💷'),
        ('💷💷💷', '💷💷💷'),
        ('💷💷', '💷💷'),
        ('💷', '💷')
     )

    name = models.CharField(max_length=255)
    position = models.CharField(
        max_length=20,
        choices=pcategory
    )
    age = models.IntegerField()
    experience = models.CharField(
        max_length=20,
        choices=CATEGORIES
    )
    skills = models.CharField(
        default='💷',
        max_length=200,
        choices=cskills
    )
    date_buyed = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['position','-skills']

    def __str__(self):
        return self.name