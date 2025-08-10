from django import forms
from .models import Review, Product


class ReviewForm(forms.ModelForm):
    """Form for creating and editing reviews on products."""
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    rating = forms.ChoiceField(choices=RATING_CHOICES, initial=3)  # Default rating set to 3

    class Meta:
        model = Review
        fields = ('rating', 'comment',)


class ProductForm(forms.ModelForm):
    """Form for creating and editing products."""

    class Meta:
        model = Product
        fields = ('name', 'brand', 'description', 'price', 'image', 'ingredients')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'ingredients': forms.Textarea(attrs={'rows': 3}),
            'price': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }
