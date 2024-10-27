from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from DjangoBasicExam.authors.forms import CreateAuthorForm
from DjangoBasicExam.authors.models import Author


class CreateAuthorView(CreateView):
    model = Author
    form_class = CreateAuthorForm
    success_url = reverse_lazy('dashboard')
    template_name = 'author/create-author.html'


