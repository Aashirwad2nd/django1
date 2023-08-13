from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("Hello. welcome to the home page")