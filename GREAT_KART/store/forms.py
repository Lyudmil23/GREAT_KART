from django import forms

from GREAT_KART.store.models import ReviewRating
# from .models import ReviewRating


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']
