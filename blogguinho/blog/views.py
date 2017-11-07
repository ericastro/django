from django.shortcuts import render

from blog.models import Post
#from django.http import HttpResponse

#def index(request):
#	return HttpResponse('Hello World!')


def index(request):
    last_posts = Post.objects.all().order_by('-created_at')[:5]

    ctx = {
        'last_posts': last_posts
    }

    return render(request, 'blog/index.html', ctx)

