from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """Form for creating and editing comments on blog posts."""
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """Form for creating and editing blog posts."""

    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image', 'excerpt')
        widgets = {
            'content': forms.Textarea(attrs={'rows': 6}),
            'excerpt': forms.Textarea(attrs={'rows': 4}),
        }
