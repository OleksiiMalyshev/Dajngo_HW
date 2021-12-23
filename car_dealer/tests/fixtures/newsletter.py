import factory

from src.apps.newsletter.models import NewsLetter


class NewLetterFactory(factory.DjangoModelFactory):
    email = 'user@gmail.com'

    class Meta:
        model = NewsLetter
