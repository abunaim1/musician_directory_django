from django.shortcuts import render,redirect
from album.forms import AlbumForm
from album.models import Album
# Create your views here.

def album(request):
    if request.method == 'POST':
        data = AlbumForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('album')
    else:
        data = AlbumForm()
    return render(request, 'album.html', {'form' : data})


def edit(request, id):
    album_ob = Album.objects.get(pk=id)
    data = AlbumForm(instance=album_ob)
    if request.method == 'POST':
        data = AlbumForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('home')
    return render(request, 'album.html', {'form' : data})

def delete(request,id):
    album_ob = Album.objects.get(pk=id)
    album_ob.delete()
    return redirect('home')