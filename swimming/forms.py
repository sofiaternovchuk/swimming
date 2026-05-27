from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'content', 'rating']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш отзыв об образовательной программе...', 'rows': 4}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 10}),
        }
        labels = {
            'author': 'Ваше имя',
            'content': 'Отзыв',
            'rating': 'Оценка (1-10)',
        }