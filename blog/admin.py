from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing blog posts.
    This class customizes the admin interface for the Post model,
    allowing for rich text editing of the content field using Summernote.
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """ Admin interface for managing blog comments. """
    list_display = (
        'comment_label', 'author', 'post', 'created_on', 'approved'
        )
    list_filter = ('approved', 'created_on', 'post')
    search_fields = ('author', 'body', 'body', 'post__title')
    actions = ['approve_comments']
    summernote_fields = ('body',)

    @admin.display(description='Comment')
    def comment_label(self, obj):
        return obj.body

    @admin.action(description="Approve selected comments")
    def approve_comments(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(request, f"{updated} comment(s) approved.")
