from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    image = CloudinaryField(blank=False)
    public_id = models.CharField(max_length=100, default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    posted_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-posted_time"]
    
    def __str__(self):
        return f"The title of Review is {self.title} | submitted by {self.user}"
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Anime(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    description = models.TextField()
    release_date = models.DateField()
    image = CloudinaryField(blank=False)
    public_id = models.CharField(max_length=100, default=0)

    class Meta:
        ordering = ["-release_date"]
    
    def __str__(self):
        return f"The title of Anime is {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    posted_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ["posted_time"]

    def __str__(self):
        return f"Comment {self.content} by {self.user_id}"
    