from django import forms

from DjangoExamPrep.albums.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['owner']