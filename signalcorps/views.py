from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from .models import Message
from .forms import MessagePost

@login_required(login_url = '/accounts/login/')
def index(request):
    if request.method == 'POST':
        form = MessagePost(request.POST)
        
        if form.is_valid():
            new_post = Message(message=request.POST['post'])
            new_post.save()
            return redirect('viewPosts')
    
    else:
        form = MessagePost()
        
    context = {'form':form}
    return render(request, 'home.html', context)

def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/accounts/login/')

#def submit_message(request):
    
def view_message(request):
    message = Message.objects.order_by('-posted_at')
    context = {'message' : message}
    return render(request, 'viewMessages.html', context)

def profile(request):
    context = {'form':form}
    return render(request, 'profile.html',context)