from django import forms

from DjangoExamPrep.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'username':
                self.fields[field].widget.attrs.update({'placeholder': 'Username'})
            elif field == 'email':
                self.fields[field].widget.attrs.update({'placeholder': 'Email'})
            elif field == 'age':
                self.fields[field].widget.attrs.update({'placeholder': 'Age'})