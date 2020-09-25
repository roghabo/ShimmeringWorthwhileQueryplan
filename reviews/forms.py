from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):

    rating = forms.IntegerField(max_value=5, min_value=1)

    class Meta:
        model = models.Review
        fields = (
            "text",
            "movie",
            "book",
            "rating",
        )

    def save(self, *args, **kwargs):
        review = super().save(commit=False)
        return review
