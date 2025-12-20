from django import forms
from.models import Book
class LoginModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
