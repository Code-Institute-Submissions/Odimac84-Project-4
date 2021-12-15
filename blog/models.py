from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from cloudinary.models import CloudinaryField


class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class Category(models.Model):
    # Model for Categories
    category_name = models.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    # Model for the Blogpost
    title = models.CharField(max_length=150)
    title_tag = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_image = CloudinaryField('image', null=True, blank=True)
    body = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    category = NameField(max_length=50,)
    likes = models.ManyToManyField(User, related_name='post_like')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    # Model for Comments
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
