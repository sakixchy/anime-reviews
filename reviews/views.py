from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Review

# Create your views here.

class PostList(generic.ListView):
    queryset = Review.objects.all()
    template_name = 'reviews/review_list.html'

def review_list(request, slug):

    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(Review, slug=slug)
    anime_title = review.title 
    return render(request, 'reviews/review_detail.html', {'review': review,  'anime_title': anime_title})