from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from community.models import CreatorProfile

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            CreatorProfile.objects.get_or_create(user=user)
            login(request, user)
            return redirect('/community/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
