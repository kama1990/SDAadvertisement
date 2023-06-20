from django.contrib import admin
from advert.models import AdvertPost 
# Register your models here.

# KROK 2
# został zaimportwaony AdvertPost ,
# musimy poinformować administartora, że stworzyliśmy nowy model , pamietając aby w konsoli wywołać python manage.py createsuperuser , bez tego nie zalogujemy się do panelu administratora
# na stronie admin - po zalogowaniu - powinien pojawic się AdvertPost

admin.site.register(AdvertPost)