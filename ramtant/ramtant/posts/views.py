from django.shortcuts import render, redirect, get_object_or_404

from django.views import View

from .models import Post

from .forms import PostForm, PostCommentForm

from django.contrib.auth.decorators import login_required

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def post_list(request):
    post_new_first = Post.objects.all().order_by('-created_at')
    post_old_first = Post.objects.all().order_by('created_at')
    
    cont = { 'posts': [post_new_first, post_old_first] }
 
    return render(request, 'posts/post_list.html', cont)

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    comments = post.comments.all()

    form = PostCommentForm()

    if request.POST:
        form = PostCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

            comment.post = post
            comment.author = request.user.profile
            
            comment.save()
            return redirect('post_detail', post_id=post.id)
    
    cont = { 'post': post, 'comments': comments, 'form': form }
    return render(request, 'posts/post_detail.html', cont)

@login_required
def post_create(request):
    if request.POST:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)

            post.author = request.user.profile

            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    
    cont = { 'form': form }

    return render(request, 'posts/post_create.html', cont )

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author.user != request.user:
        return redirect('post_list')

    if request.method == 'POST':
            post.delete()

            return redirect('post_list')
    
    cont = { 'post': post }
    
    return render(request, 'posts/delete_confirm.html', cont)

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author.user != request.user:
        return redirect('post_list')
    
    if request.POST:
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():

            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    
    cont = { 'form': form, 'post': post }

    return render(request, 'posts/post_create.html', cont )

def post_search(request):
    search = request.POST.get('search_post_field')

    if request.POST and search != '':
        search.lower()

        posts = Post.objects.filter(title__contains=search).order_by('-created_at')

        cont = {'posts': posts}

        return render(request, 'posts/post_search.html', cont )

    return redirect('post_list')