from django.db import models

# Create your models here.
# KROK 1
# Poniższa klasa została stworzona na podstawie rozpisanego działania w excelu 
# po stworzeniu klasy została została wywołana w konsoli makemigartion - która skanuje wszystkie pliki w models.py 
# nastepnie wywołano migrate - jest to komenda aby zmodyfikować bazę danych

class AdvertPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField()
    category_choices = (('1', 'bardzo ważny'), ('2', 'ważny'), ('3', 'neutralny')) # muszą być krotki i wszytsko w stringu
    category = models.CharField(max_length=15, choices=category_choices)

# po utworzonej klasie należy przejsc do pliku admin.py w tym pliku zarządzamy panelem administartora

# KROK 3

    # nazlezy stworzyc poniższą funkcję str , aby po zzarejstrowaniu w adminie, i dodaniu tam postów , pojawił nam się tytuł . z f' można dodać wiecej inofrmacji
    def __str__(self):
        return self.title
