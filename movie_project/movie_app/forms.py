from .models import Movie
from django.forms import ModelForm, Textarea, TextInput, ClearableFileInput


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'year', 'genre', 'intro', 'poster']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'year': TextInput(attrs={'class': 'form-control', 'placeholder': 'Год выхода'}),
            'genre': TextInput(attrs={'class': 'form-control', 'placeholder': 'Жанр'}),
            'intro': Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'poster': ClearableFileInput(attrs={'class': 'form-control-file'})
        }
