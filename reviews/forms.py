from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "content", "rating", "image"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
