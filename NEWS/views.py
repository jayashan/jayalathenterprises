from django.shortcuts import render

# Create your views here.

def home(request):
    context={

    }
    return render(request,'POSTS/index.html',context)
