from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """Form for creating and editing reviews on products."""
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    rating = forms.ChoiceField(choices=RATING_CHOICES, initial=3)  # Default rating set to 3

    class Meta:
        model = Review
        fields = ('rating', 'comment',)
