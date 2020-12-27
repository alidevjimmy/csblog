from django.db import models
from django.contrib.auth.models import User
import string , random


STATUS = (
    (0 , "DRAFT"),
    (1 , "PUBLISHED")
)

class Post(models.Model):
    title = models.CharField(max_length=200 ,unique=True)
    slug = models.SlugField(max_length=200 , unique=True)
    author = models.ForeignKey(User , on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to="uploads/")
    access = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
