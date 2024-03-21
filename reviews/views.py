from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Review, Comment
from .forms import ReviewForm, CommentForm


# Create your views here.

class PostList(generic.ListView):
    queryset = Review.objects.all()
    template_name = 'reviews/review_list.html'

    def get_queryset(self):
        return Review.objects.filter(status=1)

def review_list(request, slug):

    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(Review, slug=slug)
    anime_title = review.title 
    review.stars = '★' * review.rating + '☆' * (5 - review.rating)
    comments = Comment.objects.filter(review=review)

    return render(request, 'reviews/review_detail.html', {'review': review,  'anime_title': anime_title, 'comments':comments})


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
            messages.success(request, 'Your review has been submitted and is awaiting approval. ｡◕ ‿ ◕｡')
            return redirect('home') 
     else:
        form = ReviewForm()
     return render(request, 'reviews/create_review.html', {'form': form})


def my_reviews(request):
    user_reviews = Review.objects.filter(user=request.user)
    return render(request, 'reviews/my_reviews.html', {'review_list': user_reviews})

def sort_reviews(request, sort_option):

    default_sort = '-posted_time'
    queryset = Review.objects.filter(status=1)

    if sort_option == 'atoz':
        sorted_reviews = queryset.order_by('title')
    elif sort_option == 'ztoa':
        sorted_reviews = queryset.order_by('-title')
    elif sort_option == 'latest':
        sorted_reviews = queryset.order_by('-posted_time')
    elif sort_option == 'oldest':
        sorted_reviews = queryset.order_by('posted_time')
    else:
        sorted_reviews = queryset.order_by(default_sort)

    return render(request, 'reviews/review_list.html', {'review_list': sorted_reviews})


def edit_review(request, slug):
    review = get_object_or_404(Review, slug=slug)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Your review has been successfully updated.")
            return redirect('review_list', slug=review.slug)  
    else:
        form = ReviewForm(instance=review)

    return render(request, 'edit_review.html', {'form': form})


def delete_review(request, slug):
    review = get_object_or_404(Review, slug=slug)
    if request.method == 'POST':
        review.delete()
        messages.success(request, "The review has been successfully deleted.")
        return redirect('home') 
        
    return render(request, 'delete_review.html', {'review': review})

def post_comment(request, slug):
    review = get_object_or_404(Review, slug=slug)
    comments = Comment.objects.filter(review=review).order_by('-posted_time')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review  
            comment.user = request.user
            comment.save()      
    else:
        form = CommentForm()
        comments = Comment.objects.filter(review=review).order_by('-posted_time')
    return render(request, 'reviews/review_detail.html', {'review': review, 'form': form, 'comments': comments})