from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from post.models import Post, Tag, Follow, Stream, Likes
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import HttpResponseRedirect
from post.forms import NewPostform
from authy.models import Profile

# Create your views here.
@login_required
def index(request):
    user = request.user
    all_users = User.objects.all()
    folow_status = Follow.objects.filter(following=user, follower=request.user).exists()

    profile =Profile.objects.all()
    posts = Stream.objects.filter(user=user)
    group_ids = []

    for post in posts:
        group_ids.append(post.post_id)
        
    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')

    query = request.GET.get('q')
    if query:
        users = User.objects.filter(Q(username__icontains=query))

        paginator = Paginator(users, 6)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

    context = {
        'post_items': post_items,
        'follow_status': follow_status,
        'profile': profile,
        'all_users': all_users,
        }

    return render(request, 'index.html', context) 

def NewPost(request):
    user = request.user
    tags_objs= []

    if request.method == 'POST':
        form = NewPostform(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption')
            tags = form.cleaned_data.get('tags')
            tag_list= list(tag_form.split(','))

            for tag in tag_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tag_objs.append(t)
            
            p, created = Post.objects.get_or_create()
