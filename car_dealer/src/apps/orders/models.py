from django.db import models


class Order(models.Model):
    car = models.ForeignKey(
        'cars.Car',
        on_delete=models.CASCADE,
    )
    status = models.CharField(
        max_length=50,
    )
    first_name = models.CharField(
        max_length=50,
    )
    last_name = models.CharField(
        max_length=50,
    )
    email = models.EmailField(
        max_length=50,
    )
    phone = models.CharField(max_length=20,
                             null=False,
                             blank=False,
                             unique=False,
                             )
    message = models.TextField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
