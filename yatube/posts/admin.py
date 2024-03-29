from django.contrib import admin
from .models import Post, Group, Comment, Follow


class PostAdmin(admin.ModelAdmin):
    """
    Административная конфигурация для модели Post.
    """
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    """
    Административная конфигурация для модели Group.
    """
    list_display = (
        'title',
        'slug',
        'description'
    )
    search_fields = ('title',)
    list_editable = ('description',)


class CommentAdmin(admin.ModelAdmin):
    """
    Административная конфигурация для модели Comment.
    """
    list_display = (
        'id',
        'text',
    )
    search_fields = ('title',)


class FollowAdmin(admin.ModelAdmin):
    """
    Административная конфигурация для модели Follow.
    """
    list_display = (
        'user',
        'author'
    )
    search_fields = ('user', 'author',)


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
