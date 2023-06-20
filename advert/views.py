from django.shortcuts import render
from .models import AdvertPost

posts = AdvertPost.objects.all
# Create your views here.
def home(request):
    return render(request, 'home.html', {"posts": posts})