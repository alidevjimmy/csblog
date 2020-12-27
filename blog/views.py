from django.template import loader
from django.http import HttpResponse
from .models import Post

def all(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    template = loader.get_template("index.html")
    for post in posts:
        post.content = post.content[:50] + '...' if len(post.content) > 50 else post.content
    return HttpResponse(template.render({'posts' : posts}, request))


def find_post(request, slug):
    post = Post.objects.get(slug=slug)
    template = loader.get_template("find.html")
    return HttpResponse(template.render({'post':post},request))