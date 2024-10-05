from django import forms

from forumApp.posts.form_mixins import DisabledMixin
from forumApp.posts.models import Books


class BookBaseForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
        }

        error_messages = {
            'title': {
                'required': 'You must enter a title.',
                'max_length': 'Your length have to be maximum 30 characters.',
            },
        }


class AddBookForm(BookBaseForm):
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        title.capitalize()
        return cleaned_data


class EditBookForm(BookBaseForm):
    pass


class DeleteBookForm(BookBaseForm, DisabledMixin):
    disabled_fields = '__all__'


class SearchForm(forms.Form):
    title = forms.CharField(
        required=False,
        label='',
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search for book...',
        })
    )
