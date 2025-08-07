from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """Form for creating and editing reviews on products."""
    class Meta:
        model = Review
        fields = ('rating', 'comment')
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Add your review here',
                'rows': 4,
            }),
        }