from django.http import HttpResponse

# Home view
def home(request):
    return HttpResponse("Welcome to the homepage!")
