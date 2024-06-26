from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.
def index(request):
    # Create a simple html page as a string
    template = "<html>" \
                "This is your first view" \
               "</html>"
    # Return the template as content argument in HTTP response
    return HttpResponse(content=template)

def get_date(request):
    today = date.today()
    template = "<html>" \
                "Today's date is {}" \
               "</html>".format(today)
    return HttpResponse(content=template)