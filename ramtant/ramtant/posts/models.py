from django.db import models

from users.models import Profile

class Post(models.Model):
    title = models.CharField(max_length=100, default="пост")

    content = models.TextField()
    img = models.ImageField(upload_to='post_pics', null=True, blank=True)

    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PostComment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.user.username} | {self.created_at}'
    
    class Meta:
        ordering = ['created_at']