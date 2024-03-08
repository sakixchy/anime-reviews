from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(default='', max_length=100)
    content = models.TextField()
    rating = models.IntegerField()
    image = CloudinaryField()
    public_id = models.CharField(max_length=100, default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    posted_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-posted_time"]
    
    def __str__(self):
        return f"The title of Review is {self.title} | submitted by {self.user}"


class Anime(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default='', max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    image = CloudinaryField()
    public_id = models.CharField(max_length=100, default=0)

    class Meta:
        ordering = ["-release_date"]
    
    def __str__(self):
        return f"The title of Anime is {self.title}"
    


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    posted_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["posted_time"]

    def __str__(self):
        return f"Comment {self.content} by {self.user_id}"
    