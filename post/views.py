from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

from django.http import HttpResponse


def home(request):
    return HttpResponse("""
        <h1>Posting System</h1>
        <ul>
            <li><a href="/posts/">Barcha postlar</a></li>
            <li><a href="/posts/create/">Yangi post yaratish</a></li>
            <li><a href="/admin/">Admin panel</a></li>
        </ul>
    """)


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'post_form.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.id)
    else:

        form = PostForm(instance=post)

    return render(request, 'post_edit.html', {'form': form, 'post': post})


def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()

    return redirect('post_list')
