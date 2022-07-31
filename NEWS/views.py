# from django.shortcuts import render,get_object_or_404
# from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# from .models import *
# from.forms import *
# from django.urls import reverse_lazy,reverse
# from django.http import HttpResponseRedirect
#
# # Create your views here.
#
# def home(request):
#     context={
#
#
#     }
#     return render(request,"NEWS/news.html",context)
#
# class PostHomeView(ListView):
#     model = Post
#     template_name = 'NEWS/news.html'
#     # ordering = ['-id']
#     ordering = ['-publish_date']
#
#     def get_context_data(self, *args, **kwargs):
#         cat_menu=Category.objects.all()
#         context=super(PostHomeView,self).get_context_data(*args, **kwargs)
#         context['cat_menu']=cat_menu
#         return context
#
#
# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'NEWS/news_detail.html'
#
#     def get_context_data(self, *args, **kwargs):
#         cat_menu = Category.objects.all()
#         context = super(PostDetailView, self).get_context_data(*args, **kwargs)
#
#         stuff=get_object_or_404(Post,id=self.kwargs['pk'])
#         total_likes=stuff.total_likes()
#         context['cat_menu'] = cat_menu
#         context['total_likes']=total_likes
#         return context
#
#
# class AddPostView(CreateView):
#     model = Post
#     form_class = NewsForm
#     template_name = 'NEWS/add_post.html'
#     # fields = '__all__'
#     # fields = ('title','body')
#
# class AddCategoryView(CreateView):
#     model = Category
#     # form_class = NewsForm
#     template_name = 'NEWS/add_category.html'
#     fields = '__all__'
#     # fields = ('title','body')
#
# class UpdatePostView(UpdateView):
#     model = Post
#     form_class = EditNewsForm
#     template_name = 'NEWS/edit_post.html'
#     # fields = ['title','title_tag','body']
#
#
# class DeletePostView(DeleteView):
#     model = Post
#     template_name = 'NEWS/delete_post.html'
#     success_url = reverse_lazy('home_news')
#
#
# def CategoryView(request,cats):
#     category_posts=Post.objects.filter(category=cats.replace('-',' '))
#     return render(request,'NEWS/categories.html',{'cats':cats.title().replace('-',' '),'category_posts':category_posts})
#
# def LikeView(request,pk):
#     post=get_object_or_404(Post,id=request.POST.get('post_id'))
#     post.likes.add(request.user)
#     return HttpResponseRedirect(reverse('post-detail',args=[str(pk)]))
