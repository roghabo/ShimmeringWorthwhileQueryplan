from django.shortcuts import redirect, reverse, render
from . import forms, models
from django.views.generic import FormView


class CreateReviewView(FormView):

    form_class = forms.CreateReviewForm
    template_name = "reviews/detail.html"

    def form_valid(self, form):
      review = form.save()
      review.created_by = self.request.user
      review.save()
      return redirect(reverse("core:home"))

def my_review(request, pk):
  reviews = request.user.reviews.all()
  return render(request, "reviews/my_review.html",{"reviews":reviews})

def delete_review(request, pk):
  review = models.Review.objects.filter(pk=pk).delete()
  return redirect(reverse("core:home"))