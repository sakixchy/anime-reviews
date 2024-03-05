from django.contrib import admin
from .models import Anime
from .models import Review
from .models import Comment

# Register your models here.

admin.site.register(Anime)
admin.site.register(Review)
admin.site.register(Comment)