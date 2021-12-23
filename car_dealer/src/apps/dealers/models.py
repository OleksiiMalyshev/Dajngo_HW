from django.contrib.auth.models import AbstractUser
from django.db import models


class Dealer(AbstractUser):
    title = models.CharField(max_length=150)

    email = models.EmailField(
        max_length=55,
        unique=True
    )

    city = models.ForeignKey(
        'dealers.City',
        on_delete=models.CASCADE,
        default=''
    )

    class Meta:
        verbose_name = 'Dealer'
        verbose_name_plural = 'Dealers'

    def __str__(self):
        return self.title


class City(models.Model):
    name = models.CharField(max_length=40)

    country = models.ForeignKey(
        'dealers.Country',
        on_delete=models.CASCADE,
        related_name='Cities',
        default=''
    )

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=40)

    code = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name
