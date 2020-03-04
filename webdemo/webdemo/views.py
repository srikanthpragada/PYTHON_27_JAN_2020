from django.http import HttpResponse
from datetime import datetime


# Function view
def welcome(request):
    if 'name' in request.GET:
       name = request.GET['name']  # read value from name parameter
    else:
       name = "Guest"
    return HttpResponse(f"<h1 style='color:blue'>{name}, Welcome To Django!</h1>")


def now(request):
    curtime = str(datetime.now())
    return HttpResponse(f"<h1 style='color:red'>{curtime}</h1>")
