from django import forms
from album.models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'release_date' : forms.DateInput(attrs={'type' : 'datetime-local' }),
            'rating' : forms.RadioSelect()
        }