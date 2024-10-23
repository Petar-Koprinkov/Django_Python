from django import forms

from DjangoExamPrep.albums.models import Album
from DjangoExamPrep.mixins import PlaceholderMixin, ReadOnlyMixin


class BaseAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['owner']


class AddAlbumForm(PlaceholderMixin, BaseAlbumForm):
    pass


class EditAlbumForm(BaseAlbumForm):
    pass


class DeleteAlbumForm(ReadOnlyMixin, BaseAlbumForm):
    pass