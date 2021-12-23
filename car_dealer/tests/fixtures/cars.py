from uuid import uuid4

import factory
from django.core.files.base import ContentFile

from src.apps.cars.models import Car, Brand, Model, Color, Picture

from factory import fuzzy

from tests.fixtures.dealers import DealerFactory


class CarFactory(factory.DjangoModelFactory):
    model = factory.SubFactory(CarModelFactory)
    dealer = factory.SubFactory(DealerFactory)
    color = factory.SubFactory(CarColorFactory)
    picture = factory.SubFactory(CarPictureFactory)
    number = 'BC 1111 AX'
    slug = 'car nissan 78'
    engine_type = 'flat'
    pollutant_class = 'class A+'
    price = fuzzy.FuzzyInteger(1000, 15000)
    category = "Mini"
    fuel_type = "petrol"
    status = "published"
    doors = '4'
    capacity = '5'
    gear_choices = 'automatic'
    sitting_place = '5'
    first_registration_date = "2021-12-17 16:46:04.000000 +00:00"
    engine_power = fuzzy.FuzzyInteger(0, 1500)

    class Meta:
        model = Car


class CarBrandFactory(factory.DjangoModelFactory):
    name = fuzzy.FuzzyText()

    class Meta:
        model = Brand


class CarModelFactory(factory.DjangoModelFactory):
    brand = factory.SubFactory(CarBrandFactory)
    name = factory.LazyFunction(lambda: uuid4().hex)

    class Meta:
        model = Model


class CarColorFactory(factory.DjangoModelFactory):
    color = factory.SubFactory(CarFactory)
    name = "green"

    class Meta:
        model = Color


class CarPictureFactory(factory.DjangoModelFactory):
    picture = factory.SubFactory(CarFactory)
    url = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data(
                {'width': 1024, 'height': 768}
            ), 'example.jpg'
        )
    )
    position = fuzzy.FuzzyInteger()
    metadata = fuzzy.FuzzyText()

    class Meta:
        model = Picture
