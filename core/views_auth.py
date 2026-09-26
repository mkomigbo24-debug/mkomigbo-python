from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from community.models import CreatorProfile

def signup(request):
    # If already logged in, don't show signup - send to community
    if request.user.is_authenticated:
        return redirect('/community/')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = request.POST.get('username','').strip()
        
        # If username exists -> tell them to LOGIN instead (your requirement)
        if User.objects.filter(username=username).exists():
            messages.error(request, f"Account '{username}' already exists. Please LOGIN instead - you are already signed up!")
            return redirect(f"/accounts/login/?next={request.GET.get('next','/community/create/')}")
        
        if form.is_valid():
            user = form.save()
            CreatorProfile.objects.get_or_create(user=user)
            login(request, user)
            next_url = request.GET.get('next') or '/community/'
            return redirect(next_url)
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})

# Note: login view comes from django.contrib.auth.urls as /accounts/login/
# It automatically shows registration/login.html
