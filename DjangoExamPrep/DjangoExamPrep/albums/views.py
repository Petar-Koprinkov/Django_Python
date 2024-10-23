from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from DjangoExamPrep.albums.forms import AddAlbumForm, EditAlbumForm
from DjangoExamPrep.albums.models import Album
from DjangoExamPrep.utils import get_profile_object


class AddAlbumView(CreateView):
    model = Album
    template_name = 'album/album-add.html'
    form_class = AddAlbumForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.owner = get_profile_object()
        form.save()
        return super().form_valid(form)


class EditAlbumView(UpdateView):
    model = Album
    template_name = 'album/album-edit.html'
    form_class = EditAlbumForm
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'



