from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path("add_author/", views.add_author, name="add_author"),
    path("add_quote/", views.add_quote, name="add_quote"),
    path("author/<int:author_id>/", views.author_detail, name="author_detail"),
    path("tag/<str:tag_name>/", views.quotes_by_tag, name="quotes_by_tag"),
    path("quote/<int:pk>/delete/", views.delete_quote, name="delete_quote"),
    path("author/<int:pk>/delete/", views.delete_author, name="delete_author"),
]
