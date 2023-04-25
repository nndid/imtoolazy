from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=450)  # title
    author = models.ForeignKey(  # post author
        'auth.User',
        on_delete=models.CASCADE,  # delete post
    )
    body = models.TextField()  # post text

    def __str__(self):
        return self.title  # method
