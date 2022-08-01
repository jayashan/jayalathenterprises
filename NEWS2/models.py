# from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse
# from ckeditor.fields import RichTextField
# from datetime import datetime,date
# # Create your models here.
#
# class Post(models.Model):
#     title=models.CharField(max_length=255)
#     image=models.ImageField(null=True,blank=True,upload_to='images/')
#     title_tag=models.CharField(max_length=225,default='my post')
#     author=models.ForeignKey(User,on_delete=models.CASCADE)
#     # body=models.TextField()
#     body = RichTextField(blank=True,null=True)
#     publish_date=models.DateField(auto_now_add=True)
#     category=models.CharField(max_length=225,default='not_categorize')
#     likes=models.ManyToManyField(User,related_name='blog_posts')
#
#
#     def __str__(self):
#         return self.title+ '|'+ str(self.author)
#
#
#     def get_absolute_url(self):
#         # return reverse('post-detail',args=(str(self.id)))
#         return reverse('home_news')
#
#     def total_likes(self):
#         return self.likes.count()
#
# class Category(models.Model):
#     name=models.CharField(max_length=225)
#
# #
# #     def __str__(self):
# #         return self.name
# #
# #
# #     def get_absolute_url(self):
# #         # return reverse('post-detail',args=(str(self.id)))
# #         return reverse('home_news')