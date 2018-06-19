from django.shortcuts import render

# Here we create a view function that sends a view based on a given request
def home(request):
    return render(request, 'products/home.html')
