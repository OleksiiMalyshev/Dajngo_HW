from django.db import models

from django.db.models import Index


class Restaurant(models.Model):
    STATUS_OPEN = 'open'
    STATUS_CLOSED = 'closed'

    STATUS_CHOICES = (
        (STATUS_OPEN, "Open"),
        (STATUS_CLOSED, "Closed"),
    )

    title = models.CharField(max_length=30, verbose_name="Restaurant title")
    num_stars = models.IntegerField()
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default=STATUS_OPEN,
        blank=True)
    about = models.TextField()
    staff = models.ForeignKey(
        'Staff',
        on_delete=models.CASCADE,
    )
    city = models.ForeignKey(
        'City',
        on_delete=models.CASCADE,
    )
    country = models.ForeignKey(
        'Country',
        on_delete=models.CASCADE,
    )
    dish = models.ForeignKey(
        'Dish',
        on_delete=models.CASCADE,
    )
    menu = models.ForeignKey(
        'Menu',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

        indexes = [
            Index(fields=['status', ])
        ]


class Staff(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    birth_date = models.DateField()
    contacts = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, '-', {self.position}"


class Country(models.Model):
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.country


class City(models.Model):
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.city


class Dish(models.Model):
    PORTION_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    dish = models.CharField(max_length=30)
    portion_size = models.CharField(max_length=1, choices=PORTION_SIZES)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.dish


class Menu(models.Model):
    SEASON_AUTUMN = 'autumn'
    SEASON_WINTER = 'winter'
    SEASON_SPRING = 'spring'
    SEASON_SUMMER = 'summer'

    SEASON_CHOICES = (
        (SEASON_AUTUMN, "Autumn"),
        (SEASON_WINTER, "Winter"),
        (SEASON_SPRING, "Spring"),
        (SEASON_SUMMER, "Summer"),
    )

    NAME_KITCHEN = (
        ('UA', 'Ukrainian'),
        ('ITA', 'Italian'),
        ('GER', 'German'),
    )
    season = models.CharField(
        max_length=30,
        choices=SEASON_CHOICES,
        default=SEASON_SPRING,
        blank=True)
    dish_choices = models.ManyToManyField(Dish)
    name_kitchen = models.CharField(max_length=10, choices=NAME_KITCHEN)

    def __str__(self):
        return self.season
