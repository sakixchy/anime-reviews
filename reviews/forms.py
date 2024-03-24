from django import forms
from .models import Review, Comment
from django.contrib.auth.forms import UserCreationForm


class CustomSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "content", "rating", "image"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
