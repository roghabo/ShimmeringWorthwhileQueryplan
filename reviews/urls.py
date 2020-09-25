from django.urls import path
from . import views


app_name = "reviews"

urlpatterns = [
  path("create/<int:pk>", views.CreateReviewView.as_view(), name="create"),
  path("delete/<int:pk>", views.delete_review, name="delete"),
  path("<int:pk>/", views.my_review, name="review"),

]
