from . import views
from django.urls import path
from django.contrib.auth.views import LoginView


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("create_review/", views.create_review, name="create_review"),
    path("my_reviews/", views.my_reviews, name="my_reviews"),
    path("<slug:slug>/", views.review_list, name="review_list"),
    path("review/<slug:slug>/", views.review_detail, name="review_detail"),
    path("review/<slug:slug>/like/", views.like_review, name="like_review"),
    path("review/<slug:slug>/dislike/", views.dislike_review, name="dislike_review"),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("sort/<str:sort_option>/", views.sort_reviews, name="sort_reviews"),
    path("review/<slug:slug>/edit/", views.edit_review, name="edit_review"),
    path("review/<slug:slug>/delete/", views.delete_review, name="delete_review"),
    path("review/<slug:slug>/comment/", views.post_comment, name="post_comment"),
]
