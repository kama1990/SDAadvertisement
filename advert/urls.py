
from django.urls import path
from . import views

# KROK 7
# dodajemy ścięzkę detail , która będzie miał aodwołanie do views

# KROK 9
# modyfikujemy scieżkę detail , aby w zależnosci od tego , które id zostało wybrane , przekazło nam informacje o prawdiłowym poscie z details.html

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:postID>/', views.detail, name='detail')
]