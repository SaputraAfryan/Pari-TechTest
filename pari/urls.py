from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.ListBooks.as_view(), name="books"),
    path("books/<int:pk>/", views.DetailBooks.as_view(), name="books-detail"),
]
