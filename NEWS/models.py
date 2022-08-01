from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from datetime import datetime,date

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(null=True,blank=True,upload_to='images/')
    title_tag=models.CharField(max_length=225,default='my post')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    # body=models.TextField()
    body = RichTextField(blank=True,null=True)
    publish_date=models.DateField(auto_now_add=True)

    CATEGORY_CHOICES=[
        ('LOCAL','LOCAL'),
        ('BUSINESS','BUSINESS'),
        ('TRADE','TRADE'),
        ('INTERNATIONAL','INTERNATIONAL'),

    ]

    category=models.CharField(max_length=225,default='not_categorize',blank=True,null=True,choices=CATEGORY_CHOICES)



    def __str__(self):
        return self.title+ '|'+ str(self.author)

    def get_absolute_url(self):
        # return reverse('post-detail',args=(str(self.id)))
        return reverse('home_news')





class Category(models.Model):
    name=models.CharField(max_length=225)


    def __str__(self):
        return self.name


