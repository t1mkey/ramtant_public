from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required, login_required

from users.forms import UserCreationForm, ProfileEditing
from users.models import Profile, Usr

from django.views import View

from posts.models import Post

class Reg(View):

    page = 'registration/register.html'

    def get(self, request):
        cont = { 'form' : UserCreationForm() }
        return render(request, self.page, cont )
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect('/')
        
        cont = { 'form' : form }    
        return render(request, self.page, cont)

def profile(request, username=None):
    if username is None:
        profile = get_object_or_404(Profile, user = request.user)
    else:
        profile = get_object_or_404(Profile, user__username = username)

    post_new_first = Post.objects.filter(author = profile).order_by('-created_at')
    post_old_first = Post.objects.filter(author = profile).order_by('created_at')
    
    cont = { 'profile': profile, 'posts': [post_new_first, post_old_first] }

    return render(request, 'profile/profile.html', cont)

@login_required
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.POST:
        form = ProfileEditing(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            
            return redirect('my_profile')
    else:
        form = ProfileEditing(instance=profile)

    cont = { 'form': form }

    return render(request, 'profile/edit.html', cont )

@login_required
def follow(request, username):
    follow_to = get_object_or_404(Profile, user__username=username)
    usr = request.user.profile

    if follow_to == usr:
        return redirect('post_list')
    
    if not (follow_to in usr.follows.all()):
        usr.follows.add(follow_to)
    
    return redirect('profile', username=request.user.username)

@login_required
def unfollow(request, username):
    unfollow_to = get_object_or_404(Profile, user__username=username)
    usr = request.user.profile

    if unfollow_to == usr:
        return redirect('post_list')
    
    if unfollow_to in usr.follows.all():
        usr.follows.remove(unfollow_to)
    
    return redirect('profile', username=unfollow_to.user.username)