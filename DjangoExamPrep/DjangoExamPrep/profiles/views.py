from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView

from DjangoExamPrep.utils import get_profile_object


class DetailProfileView(DetailView):
    template_name = 'profile/profile-details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_profile_object()


class DeleteProfileView(DeleteView):
    template_name = 'profile/profile-delete.html'
    context_object_name = 'profile'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_profile_object()
