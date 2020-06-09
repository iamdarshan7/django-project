from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

# posts = [
#     {
#         'author': "CoryMS",
#         'title': "Blog Post 1",
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': "Jane Doe",
#         'title': "Blog Post 2",
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     },
#     {
#         'author': "Jane Austin",
#         'title': "Blog Post 3",
#         'content': 'Pride and Prejudge',
#         'date_posted': 'August 28, 1817'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})