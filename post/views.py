from django.shortcuts import get_object_or_404, render
from .models import post
# Create your views here.
def indexpage(request):
    allpost=post.objects.all()

    return render(request,'pages/index.html',{
        'post':allpost
    })


def detailpage(request,slug):
    question = get_object_or_404(post, slug=slug)

    return render(request,'pages/details.html',{'postdata': question})


def postpage(request):
    allpost=post.objects.all()

    return render(request,'pages/postg-page.html',{
        'post':allpost
    })
