from django import forms
from .models import Blog


class _BlogCreateForm(forms.Form):
    title = forms.CharField(max_length=221)
    content = forms.CharField(max_length=221)


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"

