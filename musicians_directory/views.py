from django.shortcuts import render
from album.models import Album
def home(request):
    data = Album.objects.all()
    return render(request, 'home.html', {'data':data})