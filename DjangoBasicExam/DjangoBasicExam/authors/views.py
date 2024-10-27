from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from DjangoBasicExam.authors.forms import CreateAuthorForm, EditAuthorForm
from DjangoBasicExam.authors.models import Author
from DjangoBasicExam.utils import get_profile, get_latest_post, get_all_posts


class CreateAuthorView(CreateView):
    model = Author
    form_class = CreateAuthorForm
    success_url = reverse_lazy('dashboard')
    template_name = 'author/create-author.html'


class DetailsAuthorView(DetailView):
    model = Author
    template_name = 'author/details-author.html'
    context_object_name = 'author'

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_post'] = get_latest_post()
        context['all_post'] = get_all_posts()
        return context


class EditAuthorView(UpdateView):
    model = Author
    form_class = EditAuthorForm
    success_url = reverse_lazy('details-author')
    template_name = 'author/edit-author.html'

    def get_object(self, queryset=None):
        return get_profile()


class DeleteAuthorView(DeleteView):
    template_name = 'author/delete-author.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()





