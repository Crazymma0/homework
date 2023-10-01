from django.contrib import admin

from posts.models import Post, Hashtag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "rate", "created_date", "modified_date",)
    list_filter = ("rate",)
    search_fields = ("title", "description",)
    list_editable = ("title",)


admin.site.register(Hashtag)
