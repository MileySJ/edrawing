from django.shortcuts import render

def home(request):
    return render(request, 'art_shop/home.html')
