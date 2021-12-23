import factory
from factory import fuzzy

from src.apps.orders.models import Order
from tests.fixtures.cars import CarFactory


class OrderFactory(factory.DjangoModelFactory):
    car = factory.SubFactory(CarFactory)
    first_name = "John"
    last_name = "Wolf"
    email = factory.LazyAttribute(lambda a: '{0}.{1}@example.com'.format(a.first_name, a.last_name))
    status = fuzzy.FuzzyText()
    phone = fuzzy.FuzzyInteger(0, 9, 1)

    class Meta:
        model = Order
