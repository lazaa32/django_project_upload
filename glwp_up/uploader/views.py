from django.http import HttpResponse


def index(request):
    return HttpResponse("GISlab.web uploader works!")
