from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from DjangoBasicExam.posts.forms import CreatePostForm
from DjangoBasicExam.posts.models import Post
from DjangoBasicExam.utils import get_profile


class CreatePostView(CreateView):
    model = Post
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dashboard')
    form_class = CreatePostForm

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.author = get_profile()
        return super().form_valid(form)


class DetailsPostView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'


