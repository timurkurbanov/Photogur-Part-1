from django.db import models
from django.contrib.auth.models import User

class Picture(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pictures")

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    # We want comments to be left about specific pictures, so we're giving this model a picture foreign key.
    # related_name='comments' allows us to access the relationship from both directions: my_picture.comments as well as my_comment.picture
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.message
