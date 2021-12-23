import factory
from factory import fuzzy

from src.apps import dealers
from src.apps.dealers.models import Dealer, City, Country


class DealerFactory(factory.DjangoModelFactory):


    first_name = "John"
    last_name = "Wolf"
    email = factory.LazyAttribute(lambda a: '{0}.{1}@example.com'.format(a.first_name, a.last_name).lower())
    username = factory.Sequence(lambda n: 'demo-user-%d' % n)
    password = factory.PostGenerationMethodCall('set_password', 'adm1n')
    title = fuzzy.FuzzyText()
    last_login = "2021-12-17 16:46:04.000000 +00:00"
    city_id= factory.SubFactory(CityFactory)
    is_superuser = False
    is_staff = True
    is_active = True

    class Meta:
        model = Dealer


class AdminFactory(DealerFactory):
    username = 'admin'
    is_superuser = True


class CountryFactory(factory.DjangoModelFactory):
    name = fuzzy.FuzzyText()
    code = fuzzy.FuzzyInteger(low=0, high=9999)

    class Meta:
        model ='dealers.Country'


class CityFactory(factory.DjangoModelFactory):
    name = fuzzy.FuzzyText()
    country = factory.SubFactory(CountryFactory)

    class Meta:
        model = 'dealers.City'

# class AddressFactory(factory.DjangoModelFactory):
#     address1 = fuzzy.FuzzyText()
#     address2 = fuzzy.FuzzyText()
#     zip_code = fuzzy.FuzzyInteger(low=0, high=9999)
#     city = factory.SubFactory(CityFactory)
#
#     class Meta:
#         model = Address

#
# class DealerFactory(factory.DjangoModelFactory):
#     address = factory.SubFactory(AddressFactory)
#
#     class Meta:
#         model = Dealer
