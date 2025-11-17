from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Story, Comment


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class StoryForm(forms.ModelForm):
    """
    Form for creating and editing Story objects.
    """
    class Meta:
        model = Story
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Recruiter Ghosted Me After 5 Interviews'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': (
                    'Share your experience with HR, recruiters, or the '
                    'hiring process...'
                )
            }),
        }
        labels = {
            'title': 'Story Title',
            'content': 'Your Story',
        }


class CommentForm(forms.ModelForm):
    """
    Form for creating Comment objects.
    """
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Share your thoughts or similar experience...'
            }),
        }
        labels = {
            'content': 'Your Comment',
        }
