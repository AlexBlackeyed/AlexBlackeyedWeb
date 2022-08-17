from django.shortcuts import render

# Create your views here.

from .models import Post


data = Post.objects.all()

def blog(request, post_flare=None):
    post_url = None
    if post_flare is not None:
        post_url = post_flare if "_" in str(post_flare) else None
    new_data = [d for d in data if post_flare in d.flare_choice]
    if post_flare is None and post_url is None:
        return render(request, 'blog.html', {'posts': data})
    elif post_flare is not None and post_url is None:
        return render(request, 'blog.html', {'posts': new_data})
    else:
        return render(request, 'post.html', {'posts': Post.objects.filter(post_url_title=post_url)})