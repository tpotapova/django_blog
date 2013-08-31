# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from posts.models import Post
from django.contrib import admin
def index(request):
    loggedIn = request.user.is_authenticated()
    postList = Post.objects.order_by('pub_date')
    paginator = Paginator(postList,5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    context = {'postList': postList, 'loggedIn': loggedIn,'posts':posts}
    return render(request,'posts/index.html',context)
def detail(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    return render(request,'posts/detail.html',{'post':post})
