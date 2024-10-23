from django import forms

from DjangoExamPrep.albums.models import Album


class BaseAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['owner']


class AddAlbumForm(BaseAlbumForm):
    pass
