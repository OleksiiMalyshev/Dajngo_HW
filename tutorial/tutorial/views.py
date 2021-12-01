from django.http import HttpResponse
from random import randint

def status(request):
    return HttpResponse("OK")

def rand_colour(request):
    color = "#%06x" % randint(0, 0xFFFFFF)
    return HttpResponse(color)