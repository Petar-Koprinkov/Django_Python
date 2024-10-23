from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from DjangoExamPrep.albums.forms import AddAlbumForm, EditAlbumForm, DeleteAlbumForm
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


class DetailAlbumView(DetailView):
    model = Album
    template_name = 'album/album-details.html'
    context_object_name = 'album'
    pk_url_kwarg = 'id'


class DeleteAlbumView(DeleteView):
    model = Album
    form_class = DeleteAlbumForm
    context_object_name = 'album'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    template_name = 'album/album-delete.html'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
