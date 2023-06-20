from django.shortcuts import render
from .models import AdvertPost

# KROK 4

# aby posty wyświetliły nam się na stronie , do zmiennej posts przypisujemy wszytskie obiekty z Klasy AdvertPOst - która został zaimportowana z pliku models
# w definicji prezkazaliśmy do templatki {"posts": posts}

posts = AdvertPost.objects.all
# Create your views here.
def home(request):
    return render(request, 'home.html', {"posts": posts})