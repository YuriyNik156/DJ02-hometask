from django.shortcuts import render

def carousel(request):
    return render(request, 'main/carousel.html')

def cards(request):
    return render(request, 'main/cards.html')

def accordion(request):
    return render(request, 'main/accordion.html')

def contacts(request):
    return render(request, 'main/contacts.html')