from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from DjangoBasicExam.posts.forms import CreatePostForm, DeletePostForm
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


class EditPostView(UpdateView):
    model = Post
    template_name = 'posts/edit-post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'
    form_class = CreatePostForm
    success_url = reverse_lazy('dashboard')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/delete-post.html'
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('dashboard')
    form_class = DeletePostForm

    def get_initial(self):
        return self.object.__dict__

    def get_form_kwargs(self):
        kwargs = {
            "initial": self.get_initial(),

        }
        return kwargs

    def form_invalid(self, form):
        return self.form_valid(form)
