from django.urls import path

from . import views

app_name = "smtsgg"
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("detail/<str:nickname_and_tag>", views.detail, name="detail"),
    path("match/<str:match_id>", views.match_detail, name="match")
]
