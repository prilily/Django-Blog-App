from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse



class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default= timezone.now) #add is for when created, so it can never be updates, to keep it to posted just do auto_now
    # do default which takes our timezone
    # a post only have 1 author but author many post
    author= models.ForeignKey(User, on_delete= models.CASCADE)
    # re run migrations to reflect changes
    
    #special methods with __
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

      