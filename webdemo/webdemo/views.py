from django.http import HttpResponse
from datetime import datetime


# Function view
def welcome(request):
    name = request.GET['name']  # read value from name parameter
    return HttpResponse(f"<h1 style='color:blue'>{name}, Welcome To Django!</h1>")


def now(request):
    curtime = str(datetime.now())
    return HttpResponse(f"<h1 style='color:red'>{curtime}</h1>")
