from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create_review/', views.create_review, name='create_review'),
    path('my_reviews/', views.my_reviews, name='my_reviews'),
    path('<slug:slug>/', views.review_list, name='review_list'),
    
]