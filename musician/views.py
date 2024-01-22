from django.shortcuts import render,redirect
from musician.form import MusicianForm
# Create your views here.

def musician(request):
    if request.method == 'POST':
        data = MusicianForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('musician')
    else:
        data = MusicianForm()
    return render(request, 'musician.html', {'form' : data})