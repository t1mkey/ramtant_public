from django import forms

from .models import Post, PostComment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [ 'title', 'content', 'img' ]

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = [ 'content' ]