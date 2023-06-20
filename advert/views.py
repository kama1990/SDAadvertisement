from django.shortcuts import render, get_object_or_404
from .models import AdvertPost

# KROK 4

# aby posty wyświetliły nam się na stronie , do zmiennej posts przypisujemy wszytskie obiekty z Klasy AdvertPOst - która został zaimportowana z pliku models
# w definicji prezkazaliśmy do templatki {"posts": posts}


# Create your views here.
def home(request):
    posts = AdvertPost.objects.all().order_by('category') # sortowane od najnowszych (-date)
    return render(request, 'home.html', {"posts": posts})

# KROK 6
#wprowadzamy nową stronę w aplikacji - po napisaniu funkcji przechodzimy do url oraz dodajemy templatkę

#KROK 8
# w zalzenosci od tego w który link na stronie kliniemy , kazdy z nich ma przypisany id , id zostało  przypisane do postId , które jest przekazywane z url do views a nastepnie do tempatki detail.html

def detail(request, postID):
    post = get_object_or_404(AdvertPost, id=postID)
    return render(request, 'detail.html', {'post' : post})
