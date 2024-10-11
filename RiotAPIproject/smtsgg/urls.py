from django.urls import path

from . import views

app_name = "smtsgg"
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("detail/<str:nickname>", views.detail, name="detail"),
]
