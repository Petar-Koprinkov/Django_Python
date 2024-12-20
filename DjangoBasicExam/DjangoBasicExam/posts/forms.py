from django import forms
from DjangoBasicExam.posts.mixins import PlaceholderPostMixin, ReadOnlyPostMixin
from DjangoBasicExam.posts.models import Post


class BasePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']


class CreatePostForm(PlaceholderPostMixin,BasePostForm):
    pass


class EditPostForm(BasePostForm):
    pass


class DeletePostForm(ReadOnlyPostMixin, BasePostForm):
    pass


