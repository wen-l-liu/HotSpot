from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """Form for creating and editing reviews on products."""
    class Meta:
        model = Review
        fields = ('rating', 'comment',)
