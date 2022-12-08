from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


def user_directory_path(instance, filename):
    return 'posts/{0}/{1}'.format(instance.id, filename)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CreditCard(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    image = models.ImageField(
        upload_to=user_directory_path, default='posts/mastercard.png') #eneables us to upload the sample card image
    description = models.CharField(max_length=250)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('created_on',)

    def __str__(self):
        return self.name

class User(models.Model):
    user_name = models.SlugField(max_length=250, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"Comment by {self.name}"

class Comment(models.Model):
    creditcard = models.ForeignKey(
        CreditCard, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Category, on_delete=models.PROTECT)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('created_on',)

    def __str__(self):
        return f"Comment by {self.user}"
