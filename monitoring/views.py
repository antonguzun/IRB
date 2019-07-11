from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. test There will be monitoring.")
