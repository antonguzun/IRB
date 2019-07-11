from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. There will be monitoring.")
