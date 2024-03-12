from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Review
from .forms import ReviewForm

# Create your views here.

class PostList(generic.ListView):
    queryset = Review.objects.all()
    template_name = 'reviews/review_list.html'

def review_list(request, slug):

    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(Review, slug=slug)
    anime_title = review.title 
    return render(request, 'reviews/review_detail.html', {'review': review,  'anime_title': anime_title})

def create_review(request):
    return render(request, 'reviews/create_review.html')

def my_reviews(request):
    return render(request, 'reviews/my_reviews.html')


def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  
            if request.user.is_superuser:
                review.status = 1  
            else:
                review.status = 0  
            review.save()
            messages.success(request, 'Review submitted successfully!')
            return redirect('review_detail', pk=review.pk) 
    else:
        form = ReviewForm()
    return render(request, 'reviews/create_review.html', {'form': form})