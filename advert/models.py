from django.db import models

# Create your models here.
class AdvertPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField()
    category_choices = (('1', 'bardzo ważny'), ('2', 'ważny'), ('3', 'neutralny'))
    category = models.CharField(max_length=15, choices=category_choices)

    def __str__(self):
        return self.title
