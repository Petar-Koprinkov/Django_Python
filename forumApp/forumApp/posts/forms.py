from django import forms

from forumApp.posts.models import Books


class BookBaseForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'


class AddBookForm(BookBaseForm):
    pass


