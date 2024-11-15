from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.

def post(request):
 post = Post.objects.get(id=id)
 return render(request, "blog/post.html", {'post': post})