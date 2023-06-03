from django.contrib import admin

from coreblog.models import Tag, Author, Post, Comment

# Register your models here.

admin.site.register(Tag)
admin.site.register(Author)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'email_field', 'post']


admin.site.register(Comment, CommentAdmin)
