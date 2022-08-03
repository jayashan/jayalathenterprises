from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import *
from.forms import *
from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request):
    post=Post.objects.all()
    context={
        'post':post
    }
    return render(request,'POSTS/index.html',context)


class News_Home_Page(LoginRequiredMixin,ListView):
    login_url = '../'
    model = Post
    template_name = 'POSTS/index.html'


class NewsDetailView(DetailView):
    model = Post
    template_name = 'POSTS/news_detail.html'

class AddNewsView(LoginRequiredMixin,CreateView):
    login_url = 'index.html'
    model = Post
    form_class = NewsForm
    template_name = 'POSTS/add_news.html'


class UpdateNewsView(UpdateView):
    model = Post
    form_class = EditNewsForm
    template_name = 'POSTS/edit_news.html'


class DeleteNewsView(DeleteView):
    model = Post
    template_name = 'POSTS/delete_post.html'
    success_url = reverse_lazy('home_news')