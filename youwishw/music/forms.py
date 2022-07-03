from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ClearableFileInput, HiddenInput

from .models import Song


class UploadSongForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        fields_to_change = ['author', 'views', 'pub_date', 'song_id']
        for field in fields_to_change:
            self.fields[field].widget = HiddenInput()
            self.fields[field].disabled = True

    class Meta:
        model = Song
        fields = '__all__'
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': False, 'class': 'form-control', 'accept': 'audio/mp3,audio/wav'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
          {'class': 'form-control'}
        )
        self.fields['password'].widget.attrs.update(
          {'class': 'form-control'}
        )
