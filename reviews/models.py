from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    rating = models.IntegerField()
    image = models.ImageField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    posted_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)


