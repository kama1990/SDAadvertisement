
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# KROK 7
# dodajemy ścięzkę detail , która będzie miał aodwołanie do views

# KROK 9
# modyfikujemy scieżkę detail , aby w zależnosci od tego , które id zostało wybrane , przekazło nam informacje o prawdiłowym poscie z details.html

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:postID>/', views.detail, name='detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)