from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
    Форма для создания и редактирования поста.
    """
    class Meta:
        model = Post
        fields = ('text', 'group', 'image',)


class CommentForm(forms.ModelForm):
    """
    Форма для создания комментария к посту.
    """
    class Meta:
        model = Comment
        fields = ('text',)
