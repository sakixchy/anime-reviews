from django.contrib import admin
from .models import Review
from .models import Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    list_display = ("title", "slug", "status")
    search_fields = ["title", "content"]
    list_filter = ("status", "posted_time")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


admin.site.register(Comment)
